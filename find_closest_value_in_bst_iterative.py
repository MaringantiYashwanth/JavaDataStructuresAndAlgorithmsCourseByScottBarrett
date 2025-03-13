# iterative algorithm
# Average: O(log(n)) time | O(1) space
# Worst: O(n) time | O(1) space
def find_closest_value_in_bst(tree, target):
    return find_closest_value_in_bst_helper(tree, target, closest)

def find_closest_value_in_bst_helper(tree, target, closest):
    currentNode = tree
    if abs(target.value - currentNode.value) < abs(target.value - closest.value):
        currentNode = closest.value
    elif target < currentNode.value:
        currentNode = currentNode.left
    elif target > currentNode.value:
        currentNode = currentNode.right
    else:
        break
    return closest
