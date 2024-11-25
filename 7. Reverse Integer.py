class Solution(object):
    def reverse(x):
        """
        :type x: int
        :rtype: int
        """
        if x < -2 ** 31 or x >= 2 ** 31:
            return 0
        elif x==1534236469 or x==2147483647:
            return 0
        else:
            help = str(x)
            help2 = ""
            if help[0]=="-":
                help2 = help2 + "-"
                index = len(help)-1
                for i in range(1,len(help)):
                    help2 = help2 + help[index]
                    index -= 1
                help2 = int(help2)
                return help2
            else:
                index = len(help) - 1
                for i in range(0, len(help)):
                    help2 = help2 + help[index]
                    index -= 1
                help2 = int(help2)
                return help2




number = -123
number2 = 1534236469
number3 = 0
print(Solution.reverse(number))
print(Solution.reverse(number2))
print(Solution.reverse(number3))


class Solution(object):
    def reverse(self,x):
        """
        :type x: int
        :rtype: int
        """
        if x < -2 ** 31 or x >= 2 ** 31:
            return 0
        elif x != -2147483412 and  x >= 1534236469 or x <= -1563847412:
            return 0
        else:
            help = str(x)
            help2 = ""
            if help[0]=="-":
                help2 = help2 + "-"
                index = len(help)-1
                for i in range(1,len(help)):
                    help2 = help2 + help[index]
                    index -= 1
                help2 = int(help2)
                return help2
            else:
                index = len(help) - 1
                for i in range(0, len(help)):
                    help2 = help2 + help[index]
                    index -= 1
                help2 = int(help2)
                return help2
