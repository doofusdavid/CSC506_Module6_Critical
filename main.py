from Tree import Tree

tree = Tree()
# insert with duplicates
tree.build_tree([1, 7, 4, 23, 8, 9, 4, 3, 5, 7, 9, 67, 6345, 324])
print(tree)
# Try to insert duplicate
tree.insert(7)
print(tree)
# Verify that inserts go to proper location
tree.insert(232)
print(tree)
# Try to unbalance tree
tree.insert(123)
tree.insert(122)
tree.insert(121)
tree.insert(120)
tree.insert(119)
print(tree)
