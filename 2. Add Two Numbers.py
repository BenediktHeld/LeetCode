class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        List1 = []
        List2 = []

        current = l1
        while current:
            List1.insert(0, current.val)
            current = current.next

        current2 = l2
        while current2:
            List2.insert(0, current2.val)
            current2 = current2.next

        # Konvertieren Sie die Listen in Ganzzahlen
        num1 = 0
        for digit in List1:
            num1 = num1 * 10 + digit
        num2 = 0
        for digit in List2:
            num2 = num2 * 10 + digit

        # Addieren Sie die Zahlen
        result = num1 + num2

        # Konvertieren Sie das Ergebnis zurück in eine verkettete Liste
        if result == 0:
            return ListNode(0)

        dummy = ListNode(0)
        current = dummy
        while result > 0:
            current.next = ListNode(result % 10)
            current = current.next
            result //= 10

        return dummy.next

# Erstellen Sie zwei verkettete Listen
l1 = ListNode(0)
l2 = ListNode(0)

# Erstellen Sie eine Instanz der Lösung
solution = Solution()

# Rufen Sie die addTwoNumbers-Methode auf
result_list = solution.addTwoNumbers(l1, l2)

# Geben Sie die Ergebnisliste aus
if result_list:
    current = result_list
    while current:
        print(current.val, end=" ")
        current = current.next
else:
    print("0")