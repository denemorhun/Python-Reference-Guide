'''
Level Order Binary Tree Traversal (BFS)
# Check all connections from a node

               1

            /    \

         2         3

      /    \

    4       5

output: 1 2 3 4 5

implement two functions:
    - printGivenLevel: print given level
    - printLevelorder: nodes on a given level

'''

class TreeNode: 
    def __init__(self,key): 
        self.left = None    
        self.right = None
        self.val = key 

    ###########################################
    # BFS on a binary tree
    ###########################################
    def bfs(self):
    # bfs to control children nodes

        current_node = self

        q = []
        q.append(current_node)

        while len(q) != 0:
            current_node = q.pop(0)
            print(current_node.val)
            if current_node.left:
                q.append(current_node.left)

            if current_node.right:
                q.append(current_node.right)

    ###########################################
    # DFS on a binary tree
    ###########################################
    def dfs(self, node):
        if node:
            print(node.val)
            self.dfs(node.left)
            self.dfs(node.right)

# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printInteger(n):
  print('[', n, ']', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printInteger(expected)
    print(' Your output: ', end='')
    printInteger(output)
    print()
  test_case_number += 1

if __name__ == "__main__":


    root_a = TreeNode('a')
    root_a.left = TreeNode('b')
    root_a.right = TreeNode('c')
    root_a.left.left = TreeNode('d')
    root_a.left.right = TreeNode('e')
    root_a.right.left = TreeNode('f')

    #root_a.bfs()

    # root_a.dfs(root_a)

    # need to start with level 1, lets see if we print anything
    root_a.printGivenLevel(1, 5)

    
   
    # root_1 = TreeNode(8)
    # root_1.left = TreeNode(3)
    # root_1.right = TreeNode(10)
    # root_1.left.left = TreeNode(1)
    # root_1.left.right = TreeNode(6)
    # root_1.left.right.left = TreeNode(4)
    # root_1.left.right.right = TreeNode(7)
    # root_1.right.right = TreeNode(14)
    # root_1.right.right.left = TreeNode(13)
    # expected_1 = 4
    # output_1 = visible_nodes(root_1)
    # check(expected_1, output_1)

    # root_2 = TreeNode(10)
    # root_2.left = TreeNode(8)
    # root_2.right = TreeNode(15)
    # root_2.left.left = TreeNode(4)
    # root_2.left.left.right = TreeNode(5)
    # root_2.left.left.right.right = TreeNode(6)
    # root_2.right.left =TreeNode(14)
    # root_2.right.right = TreeNode(16)

    # expected_2 = 5
    # output_2 = visible_nodes(root_2)
    # check(expected_2, output_2)

  # Add your own test cases here
  