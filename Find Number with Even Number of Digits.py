class Solution(object):
    def findNumbers(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        anzahl = 0
        for i in range(len(nums)):
            if(len(str(nums[i]))%2==0):
                anzahl += 1

        return anzahl


nums = [12,345,2,6,7896]
print(Solution.findNumbers(nums))