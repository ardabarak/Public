#include <iostream>
#include <vector>



void numberSort(std::vector<int>& array) { // function to insert sort the vector input
	for (size_t i = 0; i < array.size()-1; i++){ // for loop the input
		if (array[i] <= array[i+1]){ // it index is in place, continue
			continue;
		}
		else{ // if index number not in place
			int savedNumber = array[i]; //temp
			for (size_t k = i; k < array.size()-1; ++k){	// for (size_t k = 0; k < array.size()-1; k++){
				array[k] = array[k + 1];	// update indexes
			}
			array.pop_back();

			size_t insertPos = 0; //to insert the saved number to the correct place
			while (insertPos < array.size() && array[insertPos] <= savedNumber){ 
				insertPos++;
			}
			
			array.insert(array.begin() + insertPos, savedNumber);
			
			i = -1; 
		}
		
	}
	
} 




int main()	{
	std::cout << "oi\n";
	
	std::vector<int> unsortedArray = {9, 2, 7, 1, 3, 6, 8, 4, 5, 10};
	
	std::cout << "the unsorted array before the sorting is applied: ";
	for (int number : unsortedArray){
		std::cout << number << " ";
	}
	std::cout << "\n ";
	
	numberSort(unsortedArray);
	
	std::cout << "the unsorted array after the sorting is applied: ";
	for (int number : unsortedArray){
		std::cout << number << " ";
	}
	std::cout << "\n ";



	return 0;
}
