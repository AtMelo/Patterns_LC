from utils import *


def mergeTwoLists(list1, list2):
    head = List_Node()
    while list1 and list2:
        if list1.data > list2.data:
            head.data
    pass


link_l_1 = Single_Linked_List()
link_l_2 = Single_Linked_List()

list_vals_1 = [1, 2, 4, 8, 10]
list_vals_2 = [1, 2, 3, 9, 15]

head_1 = link_l_1.create_link_list(list_vals_1)
head_2 = link_l_2.create_link_list(list_vals_2)

while head_1:
    print(head_1.data, head_2.data)
    head_1, head_2 = head_1.next, head_2.next
