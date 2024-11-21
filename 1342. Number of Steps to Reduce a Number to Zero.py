class Solution(object):
    def numberOfSteps(self, num):
        iterations = 0
        while num >= 0:
            if (num % 2 == 0) and (num != 0):
                num = num/2
                iterations = iterations + 1
            elif (num % 2 != 0) and (num > 0):
                num = num-1
                iterations = iterations + 1
            else:
                num = num-1
        return iterations


print(Solution.numberOfSteps(10,10))