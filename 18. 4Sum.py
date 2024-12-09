class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ListOfTarget = []
        nums = sorted(nums)
        for z1 in range(len(nums) - 3):
            for z2 in range(z1 + 1, len(nums) - 2):
                for z3 in range(z2 + 1, len(nums) - 1):
                    for z4 in range(z3 + 1, len(nums)):
                        ListOfCurrent = []
                        if nums[z1] + nums[z2] + nums[z3] + nums[z4] == target:
                            ListOfCurrent.append(nums[z1])
                            ListOfCurrent.append(nums[z2])
                            ListOfCurrent.append(nums[z3])
                            ListOfCurrent.append(nums[z4])
                            checkValue = True
                            for i in range(len(ListOfTarget)):
                                if self.check_list_exists(ListOfCurrent,ListOfTarget[i]) == True:
                                    checkValue = False
                            if checkValue == True:
                                ListOfTarget.append(ListOfCurrent)
        return ListOfTarget
    def check_list_exists(self,List1,List2):
        return sorted(List1) == sorted(List2)

List = [1, 0, -1, 0, -2, 2]
solution = Solution()
List2 = solution.fourSum(List, 0)
print(List2)