from operations import *
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

            


