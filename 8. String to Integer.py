class Solution(object):
    def checkNumber(x, index):
        if index == 0 and x == "-":
            return True
        if x == "0" or  x=="1" or x=="2" or x=='3' or x=="4" or x=="5" or x=="6" or x=="7" or x=="8" or x=="9":
            return True
        else:
            return False
    def myAtoi(s):
        """
        :type s: str
        :rtype: int
        """
        newString = ""
        for i in range(len(s)):
            if Solution.checkNumber(s[i], i)==True:
                newString = newString + s[i]
        newString = int(newString)
        return newString

string = "ad334-4"
print(Solution.myAtoi(string))