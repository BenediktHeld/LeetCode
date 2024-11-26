class Solution(object):
    def maxArea(height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxNum = 0
        for i in range (len(height)):
            for y in range(i+1,len(height)):
                if maxNum < Solution.callculate_size(height,i,y):
                    maxNum = Solution.callculate_size(height,i,y)
        return maxNum

    def callculate_size(height,i,y):
        smaller = min(height[i],height[y])
        return smaller*(y-i)

height = [1,8,6,2,5,4,8,3,7]
print(Solution.maxArea(height))