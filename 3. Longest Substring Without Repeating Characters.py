class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        for i in range(len(s)):
            array = []
            length = 0
            while self.Contains(s[i], array) == True:
                array.append(s[i])
                length += 1
                i += 1
                if i >= len(s):
                    break
            if length > longest:
                longest = length
        return longest

    def Contains(self, stelle, stringLetters):
        ret = True
        for i in range(len(stringLetters)):
            if stringLetters[i] == stelle:
                ret = False
        return ret

s = "abcabcbb"

print(Solution().lengthOfLongestSubstring(s))