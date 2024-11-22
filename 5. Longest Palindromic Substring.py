class Solution(object):
    def Create_String(self, i, y, s):
        String = ""
        while i <= y:
            String = String + s[i]
            i += 1
        return String

    def Check_If_Palindrom(self, text):
        p1 = 0
        p2 = len(text) - 1
        check = True

        while p1 <= p2:
            if text[p1] != text[p2]:
                check = False
                break
            p1 += 1
            p2 -= 1
        return check

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longestSubStr = ""
        for i in range(len(s)):
            # for every place
            for y in range(i, len(s)):
                string = self.Create_String(i, y, s)
                check = self.Check_If_Palindrom(string)
                if check == True:
                    if len(longestSubStr) < len(string):
                        longestSubStr = string
        return longestSubStr


s = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
print(Solution.longestPalindrome(1,s))