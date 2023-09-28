class TreeNode:
def __init__(self, key):
self.left = None
self.right = None
self.val = key

definsert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if root.val< key:
root.right = insert(root.right, key)
        else:
root.left = insert(root.left, key)
    return root

defsearch(root, key):
    if root is None or root.val == key:
        return root
    if root.val< key:
        return search(root.right, key)
    return search(root.left, key)

defcount_occurrences(root, key):
    if root is None:
        return 0
    count = 0
    if root.val == key:
        count += 1
    count += count_occurrences(root.left, key)
    count += count_occurrences(root.right, key)
    return count

defprint_tree(root, level=0):
    if root is not None:
print_tree(root.right, level + 1)
print(" " * (level * 4) + str(root.val))
print_tree(root.left, level + 1)

root = None
root = insert(root, 50)
while(True):
key = int(input("Введите значение элемента дерева: "))
if key == 0:
        break
    else:
insert(root, key)

search_value = int(input("Введите значение для поиска: "))
result = search(root, search_value)
occurrences = count_occurrences(root, search_value)

if result:
print(f"Значение {search_value} найдено в дереве.")
print(f"Значение {search_value} не найдено в дереве.")
print(f"Значение {search_value} встречается в дереве {occurrences} раз(а).")
else:
print("Дерево:")
print_tree(root)
