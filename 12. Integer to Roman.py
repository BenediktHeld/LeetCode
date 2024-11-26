class Solution(object):
    def intToRoman(num):
        """
        :type num: int
        :rtype: str
        """
        String = ""
        while num > 0:
            if num >= 1000:
                String = String + "M"
                num = num - 1000
            elif num >= 900:
                String = String + "CM"
                num = num - 900
            elif num >= 500:
                String = String + "D"
                num = num - 500
            elif num >= 400: 
                String = String + "CD"
                num = num - 400
            elif num >= 100:
                String = String + "C"
                num = num - 100
            elif num >= 90:
                String = String + "XC"
                num = num - 90
            elif num >= 50:
                String = String + "L"
                num = num - 50
            elif num >= 40:
                String = String + "XL"
                num = num - 40
            elif num >= 10:
                String = String + "X"
                num = num - 10
            elif num >= 9:
                String = String + "IX"
                num = num - 9
            elif num >= 5:
                String = String + "V"
                num = num - 5
            elif num >= 4:
                String = String + "IV"
                num = num - 4
            elif num >= 1:
                String = String + "I"
                num = num - 1
        return String

num = 11
print(Solution.intToRoman(num))