# Driver Code

from binary_search_tree import Node, BinaryTree

####################################
# Configure tree and populate it
####################################
def setup_tree():
    # Setup Tree
    #
    # 1 - 2 - 3 - 4 - 5 - 6 - 7 - 8
    # 
    #            1
    #          /   \
    #        2      3
    #       /  \    / \
    #      4   5   6   7
    #                   \
    #                   8 
    #
    # pre:  1 -> 2 -> 4 -> 5 -> 3 -> 6 -> 7 -> 8 
    # in:   4 -> 2 -> 5 -> 1 -> 6 -> 3 -> 7 -> 8 
    # post: 4 -> 5 -> 2 -> 6 -> 8 -> 7 -> 3 -> 1

    r = Node(1)
    bt = BinaryTree(r)

    bt.root.left = Node(2)
    bt.root.right = Node(3)
    bt.root.left.left = Node(4)
    bt.root.left.right = Node(5)
    bt.root.right.left = Node(6)
    bt.root.right.right = Node(7)
    bt.root.right.right.right = Node(8)

    return bt

####################################
# Test insertion into binary tree
####################################
def test_insert():
    print("Testing insertion: ")

    bst = BinaryTree(Node(1))

    r = bst.root

    bst.insert(Node(2))
    bst.insert(Node(3))
    bst.insert(Node(4))
    bst.insert(Node(5))
    bst.insert(Node(6))
    bst.insert(Node(7))
    bst.insert(Node(8))

    print("\nPreorder")
    bst.preorder_print(r)

    print("\nInorder")
    bst.inorder_print(r)

    print("\nPostorder")
    bst.postorder_print(r)

def test_find(n):

    bst = BinaryTree(Node(1))
    r = bst.root
    

    bst.insert(Node(2))
    bst.insert(Node(3))
    bst.insert(Node(4))
    bst.insert(Node(5))
    bst.insert(Node(6))
    bst.insert(Node(7))
    bst.insert(Node(8))

    bst.root.left = Node(24)
    
    print("\nPreorder")
    bst.preorder_print(r)

    print("\nInorder")
    bst.inorder_print(r)

    print("\nPostorder")
    bst.postorder_print(r)


    print("Testing finding node, ", str(n))
    print(bst.find(n))

    print("Test if is BST satisified: ")
    print(bst.is_bst_satisfied())

    



####################################
# Test printing orders
####################################
def test_traversal_orders(bt, r):
    print("Testing print orders:")
    print("\nPreorder")
    bt.preorder_print(r)

    print("\nInorder")
    bt.inorder_print(r)

    print("\nPostorder")
    bt.postorder_print(r)

####################################
# Test printing orders
####################################
def test_level_orders(bt, r):
    print()
    # print("Testing level orders:")
    # bt.level_order_print(r)

    print("Testing reverse level order")
    bt.level_reverse_order_print(r)
 
####################################
# Test printing orders
####################################
def test_height_size(bt, r):
    print("Size of the tree ", bt.size(r))
    print("Recursive size of the tree ", bt.recursive_size(r))
    print('Height of the tree: ', bt.height(r))

####################################
# Main function
####################################
if __name__ == '__main__': 

    test_find(4)
    
    




