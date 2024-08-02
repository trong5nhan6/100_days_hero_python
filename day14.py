from collections import deque


class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert_node(root, key):
    # Create a new node
    new_node = TreeNode(key)

    # If the tree is empty, the new node becomes the root
    if root is None:
        return new_node

    # Use a queue to perform level-order traversal
    queue = []
    queue.append(root)

    # Traverse the tree
    while queue:
        # Dequeue a node
        temp = queue.pop(0)

        # Check if the left child is empty
        if temp.left is None:
            temp.left = new_node
            return root
        else:
            queue.append(temp.left)

        # Check if the right child is empty
        if temp.right is None:
            temp.right = new_node
            return root
        else:
            queue.append(temp.right)

    return root


def dfs_recursive(node):
    if node is None:
        return []

    result = []
    result.append(node.val)
    result.extend(dfs_recursive(node.left))
    result.extend(dfs_recursive(node.right))

    return result


def bfs(root):
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result


# Create the root of the tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

bfs_result = bfs(root)
print("BFS traversal result:", bfs_result)

dfs_recursive_result = dfs_recursive(root)
print("DFS (recursive) traversal result:", dfs_recursive_result)
