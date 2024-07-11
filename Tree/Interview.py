from operations import insertion
class TreeNode:
    def init(self,key):
        self.left = None
        self.right = None
        self.val = key

# Serialization --> Convert binary tree into string
def serialization(root):
    value = []
    
    def preorder(node):
        if node:
            value.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        else:
            value.append('#')
        
    preorder(root)
    return ' '.join(value)

# Deserialization --> Convert string into binary tree
def deserialization(data):
    values = iter(data.split())
    def build():
        val = next(values)
        if val == '#':
            return None
        node = TreeNode(int(val))
        node.left = build()
        node.right = build()
        
        return node
    return build()

# Ancestor of given node in binary tree
def findAncestor(root,target):
    def findAncestorHelper(node,target,path):
        if node is None:
            return False
        if node.val == target:
            return True
        if(findAncestorHelper(node.left,target,path) or findAncestorHelper(node.right,target,path)):
            path.append(node.val)
            return True
        return False
    
    path = []
    
    if findAncestorHelper(root,target,path):
        return path[::-1]
    else:
        return None

# Print boundary element of BST
def boundaryelement(root):
    result = []
    
    def leftboundary(node):
        while node:
            if not checkleaf(node):
                result.append(node.val)
            if node.left:
                node = node.left
            else:
                node = node.right
    
    def leafboundary(node):
        if node:
            leftboundary(node.left)
            if checkleaf(node):
                result.append(node.val)
            leftboundary(node.right)
    
    def rightboundary(node):
        temp = []
        while node:
            if not checkleaf(node):
                temp.append(node.val)
            if node.right:
                node = node.right
            else:
                node = node.left
        result.extend(temp[::-1])
            
    def checkleaf(node):
        return node.left is None and node.right is None
    if not root:
        return result
    if not checkleaf(root):
        result.append(root.val)
    
    leftboundary(root.left)
    leafboundary(root)
    rightboundary(root.right)
    
    return result
        
# Check that tree is balanced or not
def isbalanced(root):
    def check_height(node):
        if not node:
            return 0
        
        left_height = check_height(node.left)
        if left_height == -1:
            return -1
        
        right_height = check_height(node.right)
        if right_height == -1:
            return -1
        
        if abs(left_height-right_height) > 1:
            return -1
        
        return max(left_height,right_height)+1
    
    return check_height(root) != -1
        

# Largest value in each level of binary tree
from collections import deque
def level_wise_largest(root):
    if root is None:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        length = len(queue)
        max_val = int('-inf')
        
        for _ in range(length):
            val = queue.popleft()
            max_val = max(max_val,val)
        
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)
        result.append(max_val)
        
    return result
        

# Kth largest element in the binary tree
def k_largest_number(root):
    max_val = float('-inf')
    
    def traverse(node):
        if node is None:
            return
        
        if max_val < node.val:
            max_val = node.val
            
        traverse(node.left)
        traverse(node.right)
        
    return max_val
            

def main():
    root = None
    while True:
        print("\nChoose an operation:")
        print("1. Insert Node")
        print("2. Serialize Tree")
        print("3. Deserialize Tree")
        print("4. Find Ancestors")
        print("5. Print Boundary Elements")
        print("6. Check if Tree is Balanced")
        print("7. Largest Value in Each Level")
        print("8. Find Kth Largest Element")
        print("9. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            key = int(input("Enter value to insert: "))
            root = insertion(root, key)
            print(f"Inserted {key} into the tree.")

        elif choice == 2:
            serialized_tree = serialization(root)
            print("Serialized Tree:", serialized_tree)

        elif choice == 3:
            tree_str = input("Enter serialized tree (use '#' for None nodes): ")
            root = deserialization(tree_str)
            print("Tree deserialized successfully.")

        elif choice == 4:
            target = int(input("Enter target node value to find ancestors: "))
            ancestors = findAncestor(root, target)
            print("Ancestors of node {}: {}".format(target, ancestors))

        elif choice == 5:
            boundary = boundaryelement(root)
            print("Boundary elements of the tree:", boundary)

        elif choice == 6:
            balanced = isbalanced(root)
            print("The tree is balanced." if balanced else "The tree is not balanced.")

        elif choice == 7:
            largest_values = level_wise_largest(root)
            print("Largest values in each level of the tree:", largest_values)

        elif choice == 8:
            k_largest = k_largest_number(root)
            print("Kth largest value in the tree:", k_largest)

        elif choice == 9:
            break

        else:
            print("Invalid choice!")
            
if __name__ == "__main__":
    main()
            


