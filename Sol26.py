# 26. Remove Duplicates from Sorted Array
# faster::
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        insert = 1
        for i in range(0,len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[insert] = nums[i+1]
                insert += 1
        return insert

# tested::
def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    solList = []
    dupList = []
    k = 0
    for i in range(len(nums)):
        if nums[i] not in solList:
            k += 1
            solList.append(nums[i])
        elif nums[i] in solList:
            # print("Hop")
            nums[i] = '_'
            dupList.append(nums[i])
        # print("solList: ", solList)
        # print("dupList: ", dupList)

    nums[:] = solList + dupList
    print("nums sorted: ", nums)
    # print("K: ", k)
    return k

nums = [1,1,2]
# nums =[0,0,1,1,1,2,2,3,3,4]

removeDuplicates(nums)