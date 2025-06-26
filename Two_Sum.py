# Two Sum
def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        targetlist = []

        for i in range(len(nums)):
                print("i: ", i)
                print("nums[i]: ", nums[i])
                if ((target - (nums[i])) in (nums[:i] + nums[i+1:])): 
                        targetlist.append(i)
        return targetlist