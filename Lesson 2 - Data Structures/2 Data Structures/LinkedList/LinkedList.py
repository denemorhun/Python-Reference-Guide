'''
Linked list
Every node has  -> Value: the data
                -> Next: a pointer to the next Node
LinkedList starts with a head node
(Assume data entries are unique).
'''
#########################################
# The Node Class
#########################################
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"Node: {self.data}"

#########################################
# The LinkedList Class
#########################################
class LinkedList:
    def __init__(self):  
        self.head = None

    #########################################
    # Print details of Node
    #########################################
    def print_helper(self, node, name):
        if node is None:
            print(name + ": None")
        else:
            print(name + ":" + node.data)

    #########################################
    # insert at the end of the list (append)
    #########################################
    def append(self, data):
        new_node = Node(data)

        # if there is no head node, set new_node to head none
        if self.head is None:
        #    print("No existing head node. \nInserting", new_node, "as head.")
            self.head = new_node
            return

        # if a node exists, set the last known node to head
        last_node = self.head

        # scroll through nodes until we get to the last node
        while last_node.next is not None:
            last_node = last_node.next

        # print("Appending", new_node)
        last_node.next = new_node  

    #########################################
    # insert at the beginning of the list (prepend)
    #########################################
    def prepend(self, data):
        new_node = Node(data)
    
        if self.head is None:
        #    print("No existing head node. \nInserting ", new_node)
            self.head = new_node
            return

        # set the next pointer to the old head
        new_node.next = self.head
        # set the new_node to be head
        # print("Prepending", new_node)
        self.head = new_node 

    #########################################
    # insert after a given node: data, value 
    # (B, Z) would mean insert Z after B
    #########################################
    def insert_after_node(self, data, target):

        # This section is broken
        if not target:
            print("Node value is not found.")
            return

        new_node = Node(data)
        
        # set the next pointer of new node to proceeding node after target
        new_node.next = target.next
        # reconnect the next pointer of the current node to the new node
        print("Inserting", new_node, "after", target)
        target.next = new_node   

    #########################################
    # delete an item from the list
    #########################################
    def delete_node(self, data):

        current_node = self.head

        # Case head node:
        if current_node.data == data and current_node is not None:
            print("Found an head node to delete:", current_node.data)
        
            #set the new head node to the next node
            print("Deleting node -> " + data)
            self.head = current_node.next
            current_node = None
            return

        while current_node and current_node.data != data:
            preceeding_node = current_node
            current_node = current_node.next

        if current_node is None:
            return

        print("Found a matching node to delete", current_node)
        print("Deleting node ->", current_node)

        preceeding_node.next = current_node.next
        current_node = None

    ######################################### 
    # delete at position
    ##########################################
    def delete_at(self, pos):
        # start at head and counting
        current_node = self.head
        pos_count = 0

        if current_node is None:
            return
        
        # if asked to remove head node
        if pos == 0:
            self.head = current_node.next
            current_node = None
            return

        while pos_count != pos and current_node is not None:
            preceeding_node = current_node
            current_node = current_node.next
            pos_count += 1

        # print(f'Deleting node -> {current_node}, at position {pos_count}')
        preceeding_node.next = current_node.next
        current_node = None
    
    #########################################
    # Length
    #########################################
    def length (self):
        count = 0
        current_node = self.head
        
        # if head node is null, length is 0
        if current_node is None:
            return count

        while current_node is not None:
            count += 1
            current_node = current_node.next
            
        return count 

    # where node is the head node
    def length_recursive(self, node):
        if node is None:
            return 0
        else:
            return self.length_recursive(node.next) + 1


    #########################################
    # Node swap 2 cases:
    # 1. Node_1 and Node_2 are not head nodes.
    # 2. Either Node_1 or Node_2 are head nodes.
    #########################################
    def swap_nodes(self, key_1, key_2):

        # if the keys are identical no need to do anything
        if key_1 == key_2:
            return

        prev_1 = None
        # start at the head and scroll through the list
        curr_1 = self.head

        # while the current head hasn't reached the end
        # While the current head isn't first key to be swapped
        # when loop ends, we end up with the prev node and first node to be swapped
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next
        
        prev_2 = None
        # start at the head and scroll through the list
        curr_2 = self.head

        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next

        if not curr_1 or not curr_2:
            return

        # Node 1 is not a head node
        if prev_1 is not None:
            # point the previous node to node to be swapped
            prev_1.next = curr_2
        # Node 1 is a head node
        else:
            self.head = curr_2
            
        # Node is not a head node
        if prev_2 is not None:
            # point the previous node to node to be swapped
            prev_2.next = curr_1
        else:
            self.head = curr_1

        # swap the next nodes to reconnect the list
        curr_1.next, curr_2.next = curr_2.next, curr_1.next

    #########################################
    # Reverse order of List
    #########################################
    def reverse_list_iterative(self):

        current_node = self.head
        prev_node = None

        #while current node is Not None, scroll
        while current_node:
            # create a pointer to the next node
            next_node = current_node.next

            # point the next node to the previous node
            current_node.next = prev_node

            # set prev node to the current to proceed
            prev_node = current_node

            current_node = next_node

        # set the last instance of prev_node as head node (i.e. E)
        self.head = prev_node


    ################################################
    # Merge two lists using three pointers
    # P 1st list head, Q 2nd list head
    # S keep track of the lesser value
    ################################################
    def merge_with(self, list2):

        p = self.head
        q = list2.head

        new_list = LinkedList()

        if not p:
            return q
        
        if not q:
            return p

        if p and q:
            while p.next and q.next:
                if p.data < q.data:
                    s = p
                    p = p.next
                elif q.data < p.data:
                    s = q
                    q = q.next
                
                new_list.append(s)

        return new_list

    #########################################
    # print out the data
    #########################################
    def print_list(self):
        current_node = self.head
        if current_node is None:
            print("Empty linkedlist")
        
        print("Printing the entire list:")
        # scroll the list until we reach the end
        while current_node is not None:
            print (current_node.data)
            current_node = current_node.next

    #########################################
    # clear the list
    #########################################
    def clear_list(self):
    # scroll through the whole list and set everything to None
        current_node = self.head

        if current_node is None:
            print("Empty linkedlist")
            return
        
        print("Clearing the entire list.")
        # scroll the list until we reach the end
        for current_node in range (self.length()):
            # move pointer to the next node
            current_node = None


#########################################
# Create a linked list and run tests
#########################################

def main():
    setup_linkedlist_2()
    new_list = itemlist2.merge_with(itemlist3)
    new_list.print_list()

    
def setup_linkedlist():
    global itemlist
    itemlist = LinkedList()

    # append and prepend some items -> (A, B, C, D, E)
    itemlist.append("C")
    itemlist.append("D")
    itemlist.prepend("B")
    itemlist.append("E")
    itemlist.prepend("A")

def setup_linkedlist_2():
    global itemlist2
    global itemlist3
    itemlist2 = LinkedList()
    itemlist3 = LinkedList()

    # append and prepend some items
    itemlist2.append("6")
    itemlist2.append("8")
    itemlist2.prepend("4")
    itemlist2.append("10")
    itemlist2.prepend("2")

    # append and prepend some items
    itemlist3.append("5")
    itemlist3.append("7")
    itemlist3.prepend("3")
    itemlist3.append("9")
    itemlist3.prepend("1")

def test_length():
    # print the length -> 5
    print("Length:", itemlist.length())

def test_delete():

    # delete an item
    itemlist.delete_node('0 Rh+')
    itemlist.delete_node('B')
    itemlist.delete_at(3)

# a, b = b, a
def test_swap():

    setup_linkedlist()
    
    itemlist.swap_nodes("B", "C")
    itemlist.swap_nodes("A", "E")
    itemlist.swap_nodes("A", "A")

    itemlist.print_list()

def test_reverse():
    setup_linkedlist()
    itemlist.print_list()

    itemlist.reverse_list_iterative()
    itemlist.print_list()

    itemlist.reverse_list_iterative()
    itemlist.print_list()

if __name__ == "__main__":
    main()