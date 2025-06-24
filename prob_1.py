
"""
inputArr, represents the array with inputArr_size (N) elements.
"""
def funcSum(inputArr):
	# Write your code here
	biggestNom = max(inputArr)
	if (biggestNom <= 0): 	# if the biggest number is negative then return that
		return biggestNom 


	currntBiggest = 0
	globalBiggest = 0
	for i in inputArr:
		currntBiggest = max(i, currntBiggest + i)			# saving the max of current biggest sum and the current+index
		globalBiggest = max(currntBiggest, globalBiggest)	# saving the sum if it changes globally

	return globalBiggest

def main():
	#input for inputArr
	inputArr = []	
	print("input the size of array svp: ")
	inputArr_size  = int(input())               # taking input the size of the list
	print("input the numbers with spaces svp: ")
	inputArr = list(map(int,input().split()))   # taking input the elements of the list (separated by spaces)
	
	
	result = funcSum(inputArr)
	print(result)	

if __name__ == "__main__":
	main()