class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = str(num)
        NewSum = int(num)
        while NewSum >= 10:
            NewSum = 0
            for i in range(len(num)):
                NewSum = NewSum + int(num[i])
            num = str(NewSum)
        return NewSum

num = 38
print(Solution.addDigits(1,num))