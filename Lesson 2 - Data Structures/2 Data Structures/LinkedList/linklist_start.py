# Linked list example


# the Node class
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def get_data(self):
        return self.val

    def set_data(self, val):
        self.val = val

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


# the LinkedList class
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.count = 0

    def get_count(self):
        return self.count

    def insert(self, data):
        # insert a new node
        new_node = Node(data)
        # set the head as next node
        new_node.set_next(self.head)
        # point head to the new node
        self.head = new_node
        # increment count
        self.count += 1


    def find(self, val):
        # find the first item with a given value
        item = self.head
        while (item != None):
            if item.get_data() == val:
                print("Value found: ", val )
                return item
            else:
                # if item is not what we want assign next item
                item = item.get_next()
        # if we don't find any item 
        print("Value cannot be found:", val)   
        return None

    def deleteAt(self, idx):
        # delete an item at given index
        # if index is greater than length exit
        if idx > self.count:
            print("index out of bounds")
            return

        # if list is null exit
        if self.head == None:
            return
        else:
            tempIdx = 0
            #make a temp node
            node = self.head
            # we want to scroll to the one just before the value at the index to be deleted
            while tempIdx < idx-1:
                node = node.get_next()
                tempIdx += 1
            # do not understand here.
            # once we found the previous node to the one we want to get rid of, set its next field to point to the node that's after the one we want to delete
            node.set_next(node.get_next().get_next())
            #decrement to reflect deletion
            self.count -= 1


    def dump_list(self):
        # print the whole list
        tempnode = self.head
        while (tempnode != None):
            print("Node: ", tempnode.get_data())
            tempnode = tempnode.get_next()


# create a linked list and insert some items
itemlist = LinkedList()
itemlist.insert(38)
itemlist.insert(49)
itemlist.insert(13)
itemlist.insert(15)
itemlist.dump_list()

# exercise the list
print("Item count: ", itemlist.get_count())
print("Finding item: ", itemlist.find(13))
print("Finding item: ", itemlist.find(78))

# delete an item
itemlist.deleteAt(6)
itemlist.deleteAt(3)
print("Item deleted at 3")
print("Item count: ", itemlist.get_count())
print("Finding item: ", itemlist.find(38))
itemlist.dump_list()