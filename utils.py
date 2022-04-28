# Create Linked list
class List_Node:
    def __init__(self, val=0):
        self.data = val
        self.next = None

    def has_value(self, value):
        """ method to compare the value with the node data"""
        if self.data == value:
            return True
        else:
            return False


class Single_Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def create_link_list(self, list_vals: list):
        for val_i in list_vals:
            new_node = List_Node(val_i)
            if self.head is None:
                self.head = new_node
            else:
                cur = self.head
                while cur.next:
                    cur = cur.next
                cur.next = new_node
                # link_l.tail.next = new_Node
            # link_l.tail = new_Node
        return self.head
