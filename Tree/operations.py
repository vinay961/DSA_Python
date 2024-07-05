class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Insertion in BST(Binary Search Tree)
def insertion(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if root.val < key:
            root.right = insertion(root.right, key)
        else:
            root.left = insertion(root.left, key)
    return root

# Search in BST(Binary Search Tree)
def search(root, key):
    if root is None or root.val == key:
        return root
    if root.val < key:
        return search(root.right, key)
    else:
        return search(root.left, key)

# Helper function for deletion
def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

# Deletion of node in BST
def deletion(root, key):
    if root is None:
        return root
    if root.val < key:
        root.right = deletion(root.right, key)
    elif root.val > key:
        root.left = deletion(root.left, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        
        temp = minValueNode(root.right)
        root.val = temp.val
        root.right = deletion(root.right, temp.val)
    return root

# Height of BST
def height(root):
    if root is None:
        return 0
    left_height = height(root.left)
    right_height = height(root.right)
    return max(left_height, right_height) + 1

# Checking given BST is valid or not
def check_BST(root, min_val=float('-inf'), max_val=float('inf')):
    if root is None:
        return True
    if root.val <= min_val or root.val >= max_val:
        return False
    return check_BST(root.right, root.val, max_val) and check_BST(root.left, min_val, root.val)

# Inorder traversal
def inorder_traversal(root):
    if root is None:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)

# Levelorder traversal
from collections import deque
def levelorder_traversal(root):
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

def main():
    root = None
    
    while True:
        print("\n--- Binary Search Tree Operations ---")
        print("1. Insert")
        print("2. Search")
        print("3. Delete")
        print("4. Check Height")
        print("5. Check if Valid BST")
        print("6. Inorder Traversal")
        print("7. Level Order Traversal")
        print("8. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            key = int(input("Enter value to insert: "))
            root = insertion(root, key)
            print(f"Inserted {key} into the BST.")
        
        elif choice == 2:
            key = int(input("Enter value to search: "))
            result = search(root, key)
            if result:
                print(f"{key} is found in the tree.")
            else:
                print(f"{key} is not found in the tree.")
        
        elif choice == 3:
            key = int(input("Enter value to delete: "))
            root = deletion(root, key)
            print(f"Deleted {key} from the BST.")
        
        elif choice == 4:
            print(f"Height of the BST: {height(root)}")
        
        elif choice == 5:
            if check_BST(root):
                print("The tree is a valid BST.")
            else:
                print("The tree is not a valid BST.")
        
        elif choice == 6:
            print("Inorder Traversal of the BST:", inorder_traversal(root))
        
        elif choice == 7:
            print("Level Order Traversal of the BST:", levelorder_traversal(root))
        
        elif choice == 8:
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
