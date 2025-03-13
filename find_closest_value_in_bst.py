# recursive algorithm
# Average Time Complexity: O(Log(n)) time | O(log(n)) space
# Worst time complexity: O(n) time | O(n) space
def find_closest_value_in_bst(tree, target):
    return find_closest_value_in_bst_helper(tree, target, closest)

def find_closest_value_in_bst_helper(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(tree.value - target):
        closest = tree.value
    elif closest < tree.value:
        find_closest_value_in_bst_helper(tree.left, target, closest)
    elif closest > tree.value:
        find_closest_value_in_bst_helper(tree.rigth, target, closest)
    else:
        return closest
