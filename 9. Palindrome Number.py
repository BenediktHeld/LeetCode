class Solution(object):
    def isPalindrome(self, text):
        p1 = 0
        p2 = len(str(text)) - 1
        result = True
        while p1 < p2:
            if text[p1]!=text[p2]:
                result = False
                return result
            else:
                p1+=1
                p2-=1
        return result


solution = Solution()
print(solution.isPalindrome("TexeT"))