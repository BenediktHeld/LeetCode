class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        CurrentPos = 0
        current = nums[CurrentPos]
        #Search
        while True:
            if current == target:
                return CurrentPos
            elif current > target:
                return CurrentPos
            elif CurrentPos < len(nums)-1:
                CurrentPos = CurrentPos + 1
                current = nums[CurrentPos]
            else:
                return len(nums)

nums = [1,3,5,6]
target = 2

print(Solution.searchInsert(1,nums,target))