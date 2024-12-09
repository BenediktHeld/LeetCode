class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Create a dummy node to simplify the merging process
        dummy = ListNode()
        current = dummy

        # Traverse both lists and merge them
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # If there are remaining nodes in either list, append them
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        # Return the merged list, which starts from the next of the dummy node
        return dummy.next


# Helper function to create a linked list from a list
def create_linked_list(elements):
    dummy = ListNode()
    current = dummy
    for element in elements:
        current.next = ListNode(element)
        current = current.next
    return dummy.next


# Helper function to convert a linked list to a list
def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


# Example usage
list1 = create_linked_list([1, 2, 4])
list2 = create_linked_list([1, 3, 4])
solution = Solution()
merged_list = solution.mergeTwoLists(list1, list2)
print(linked_list_to_list(merged_list))  # Output: [1, 1, 2, 3, 4, 4]
