from utils import *


def reverseList(head: List_Node) -> List_Node:
    """
    Given the head of a singly linked list, reverse the list, and return the reversed list.
    """

    prev = None
    current = head
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    head = prev
    return head


# Method to reverse the list
def reverse(head):
    # If head is empty or has reached the list end
    if head is None or head.next is None:
        return head

    # Reverse the rest list
    rest = reverse(head.next)

    # Put first element at the end
    head.next.next = head
    head.next = None

    # Fix the header pointer
    return rest


list_1 = [1, 2, 3, 4, 5, 6]
linked_l = Single_Linked_List()
head_ll = linked_l.create_link_list(list_1)

revers_ll = reverse(head_ll)

while revers_ll:
    print(revers_ll.data)
    revers_ll = revers_ll.next

# Runtime: 76 ms, faster than 7.30% of Python3 online submissions for Reverse Linked List.
# Memory Usage: 15.4 MB, less than 57.38% of Python3 online submissions for Reverse Linked List.
