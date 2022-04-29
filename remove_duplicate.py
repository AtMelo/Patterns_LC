from LC.Patterns_LC.utils import List_Node
from utils import *


def deleteDuplicates(head: List_Node) -> List_Node:
    """
    Given the head of a sorted linked list, delete all duplicates
    such that each element appears only once. Return the linked list
    sorted as well.
    """
    temp = List_Node()
    temp.next = head
    cur = head
    prev = temp
    mem_val = None
    while cur:
        if cur.data != mem_val:
            mem_val = cur.data
            prev = prev.next
        else:
            prev.next = cur.next
        cur = cur.next
    return temp.next


list_1 = [1, 2, 2, 3, 4, 4, 5, 6, 6]

linked_l = Single_Linked_List()
head_ll = linked_l.create_link_list(list_1)

clear_link_l = deleteDuplicates(head_ll)

# Visualisation
while clear_link_l:
    print(clear_link_l.data)
    clear_link_l = clear_link_l.next

# Runtime: 45 ms, faster than 78.33% of Python3 online submissions for Remove Duplicates from Sorted List.
# Memory Usage: 14 MB, less than 30.65% of Python3 online submissions for Remove Duplicates from Sorted List.
