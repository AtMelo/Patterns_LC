from utils import *


def removeElements(head_link_l, val):
    temp = List_Node()
    temp.next = head_link_l
    cur = head_link_l
    prev = temp
    while cur:
        if cur.data == val:
            prev.next = cur.next
        else:
            prev = prev.next
        cur = cur.next
    return temp.next


list_1 = [1, 2, 6, 3, 4, 5, 6]

linked_l = Single_Linked_List()
head_ll = linked_l.create_link_list(list_1)

clear_link_l = removeElements(head_ll, 6)

# Visualisation
while clear_link_l:
    print(clear_link_l.data)
    clear_link_l = clear_link_l.next

# Result:
# Runtime: 65 ms, faster than 95.21% of Python3 online submissions for Remove Linked List Elements.
# Memory Usage: 17.8 MB, less than 82.33% of Python3 online submissions for Remove Linked List Elements.
