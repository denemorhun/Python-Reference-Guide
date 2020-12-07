# Denem Orhun

def findClosestValueInBst(tree, target) -> int:
    print("Target: " , target)
    # we need a helper function to call recursively
    # tree.value starts with root
    closest = _findClosestValueInBst(tree, target, tree.value)
    print ("This is our closest: " ,closest)
    return closest
    

# closest is a value of a node
def _findClosestValueInBst(tree, target, closest) -> int:
	
	# if the difference between target and current node 
	# is less that established difference between 
	# closest and target, update closest node
	diff = abs(closest - target)
	
	if abs(target - tree.value) < diff:
		print("Updating the closest value")
		closest = tree.value
	else:
		print("Eliminating half of tree")
	
	# If target value is more than current node, traverse right
	if target > tree.value:
		print("Traversing Right tree, starting with", tree.value)
		return _findClosestValueInBst(tree.right, target, closest)
	# if target value is less than current node, traverse left
	elif target < tree.value:
		print("Traversing Left tree, starting with", tree.value)
		return _findClosestValueInBst(tree.left, target, closest)
	# If target and closest are equal 
	else:
		return closest

	
# This is the class of the input tree. Do not edit
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
