class Solution(object):
    def findMaxConsecutiveOnes(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest = 0
        for i in range(len(nums)):
            current = i
            length=1
            if (length(nums)==1) and (nums[0]==0):
                return 0
            while (current<(len(nums)-1)) and (nums[current] == nums[current+1]) and (nums[current] != 0):
                length += 1
                current += 1
            if longest < length:
                longest = length
        return longest

nums = [0]
print(Solution.findMaxConsecutiveOnes(nums))