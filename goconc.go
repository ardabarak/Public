package main

import (
	"fmt"
	"sync"
)

type Task struct {
	Number int
	Turn   int
	Done   bool
}

func printer(id int, suffix string, ch <-chan Task, chOut chan<- Task, wg *sync.WaitGroup) {
	defer wg.Done()

	for task := range ch {
		if task.Done {
			fmt.Printf("-- [Routine %d] Exiting...\n", id)
			chOut <- task
			return
		}

		if task.Turn == id {
			fmt.Printf("%d (printed from %s)\n", task.Number, suffix)

			if task.Number >= 25 { //telling the others to exit
				chOut <- Task{Done: true}
				return
			}

			nextTurn := (id % 4) + 1 //passing to next routine
			chOut <- Task{Number: task.Number + 1, Turn: nextTurn}
		} else {
			chOut <- task //just passing it on
		}
	}
}

var wg sync.WaitGroup

func main() {
	//Channels
	ch1 := make(chan Task)
	ch2 := make(chan Task)
	ch3 := make(chan Task)
	ch4 := make(chan Task)

	wg.Add(3)

	//Starting goroutines with trace messages
	go printer(1, "1st routine", ch1, ch2, &wg)
	go printer(2, "2nd routine", ch2, ch3, &wg)
	go printer(3, "3rd routine", ch3, ch4, &wg)
	go printer(4, "4th routine", ch4, ch1, &wg)

	fmt.Println("- [Main] Starting the routine chain...")
	ch1 <- Task{Number: 1, Turn: 1}

	//Waiting for all routines to exit
	wg.Wait()

	//Closing all channels to release memory
	close(ch1)
	close(ch2)
	close(ch3)
	close(ch4)

	fmt.Println("- [Main] All routines completed & exited.")
}
