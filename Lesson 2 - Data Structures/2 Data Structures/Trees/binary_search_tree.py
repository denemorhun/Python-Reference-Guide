from queue import Queue

# Node Class
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
# Binary Tree Class
class BinaryTree:
    def __init__(self, root):
        self.root = root

    ##################################
    # Root -> Left -> Right
    ##################################
    def preorder_print(self, root):
        if root:
            print(str(root.data), end=' -> ')
            self.preorder_print(root.left)
            self.preorder_print(root.right)

    ##################################
    # Left -> Root -> Right
    ##################################
    def inorder_print(self, root):
        if root:
            self.inorder_print(root.left)
            print(str(root.data), end=' -> ')
            self.inorder_print(root.right)

    ##################################
    # Left -> Right -> Node
    ##################################
    def postorder_print(self, root):
        if root:
            self.postorder_print(root.left)
            self.postorder_print(root.right)
            print(str(root.data), end=' -> ')

    ##################################
    # Node -> Left -> Right 
    ##################################
    def level_order_print(self, root):
        if root:
            q = Queue()
            q.put(root)

            while not q.empty():
                node = q.get_nowait()

                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)

                print(str(node.data), end=' -> ')

    ##################################
    # Left -> Right -> Node
    # Reverse Level Order using stack
    # 8 -> 4 -> 5 -> 6 -> 7 -> 2 -> 3 -> 1 
    ##################################
    def level_reverse_order_print(self, root):
        if root:
            stack = []
            stack.append(root)

            i = 0 

            # populate stack 
            while i < len(stack):
                node = stack[i]
                
                # must put right child node first
                if node.right:
                    stack.append(node.right)

                if node.left:
                    stack.append(node.left)
        
                i+=1

            while len(stack) > 0:
                print(stack.pop().data, end= " -> ")

    ####################################
    # Calculate Size of the Binary Tree
    ####################################
    def size(self, root):
        size = 0 

        if root:
            stack = []
            stack.append(root)

            # populate stack 
            while size < len(stack):
                node = stack[size]
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
                size+=1

            return size

    ####################################
    # Calculate Size of the Binary Tree
    ####################################
    def recursive_size(self, root):
        if root is None:
            return 0
        # Return size of left tree + size of right tree
        return self.recursive_size(root.left) + self.recursive_size(root.right) + 1
    
    ######################################
    # Calculate Height of the Binary Tree
    # Node is height 0
    #####################################
    def height(self, root):
        if root is None:
            return -1
        # pick max of all subtrees to the left and all subtrees on the right
        return max(self.height(root.left), self.height(root.right)) + 1

    ######################################
    # Insert value into Binary Tree
    #####################################
    # If Node value is less than root, insert to left
    # If Node value is more than root, insert to right
    def insert(self, node):
        if self.root is None:
            self.root = node
        else:
            self._insert(node.data, self.root)
    # recursive call to reach the end where a null node is found  
    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            # recursively call function until we find a null node
            else:
                self._insert(data, cur_node.left)

        elif data > cur_node.data:
            if cur_node.right is None:
                    cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)

        else:
            print("The value is already present in the tree.")

    ######################################
    # Return true if input value is found
    #####################################
    def find(self, data) -> bool:
        if self.root:
            # check all values starting with root
            is_found = self._find(data, self.root)
            if is_found == True:
                return True
            else:
                return False
        else: 
            print("No nodes found in tree.")
            return None

    def _find(self, data, cur_node):
        # recursively check all nodes less than node value
        if data < cur_node.data and cur_node.left:
            return self._find(data, cur_node.left)   
        # recursively check all nodes more than node value
        elif data > cur_node.data and cur_node.right:
            return self._find(data, cur_node.right)

        if data == cur_node.data:
            return True

    '''
    Conditions for BST:
    # All nodes left of node must have values less than node
    # All nodes right of node must have values more than node
    # Parent nodes have at most 2 children

    '''
    def is_bst_satisfied(self) -> bool:
        if self.root:
            is_bst = self._is_bst_satisfied(self.root)
            if is_bst == True:
                return True
            else:
                return False
        else:
            print("No nodes found in tree.")
            return None
    
    def _is_bst_satisfied(self, cur_node):

        if cur_node.left:
            if cur_node.data > cur_node.left.data: 
                self._is_bst_satisfied(cur_node.left)
            else:
                return False
            return True
        elif cur_node.right:
            if cur_node.data < cur_node.right.data:
                self._is_bst_satisfied(cur_node.right)
            else:
                return False
            return True
        else:
            return False


        


        



    