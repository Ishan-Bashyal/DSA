class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = TreeNode('R')
nodeA = TreeNode('A')
nodeB = TreeNode('B')
nodeC = TreeNode('C')
nodeD = TreeNode('D')
nodeE = TreeNode('E')
nodeF = TreeNode('F')
nodeG = TreeNode('G')

root.left = nodeA
root.right = nodeB
nodeA.left = nodeC
nodeA.right = nodeD
nodeB.left = nodeE
nodeB.right = nodeF
nodeF.left = nodeG

def inorder_dfs(node):
    if node:
        inorder_dfs(node.left)
        print(node.data, end=' ')
        inorder_dfs(node.right)

def preorder_dfs(node):
    if node:
        print(node.data, end=' ')
        preorder_dfs(node.left)
        preorder_dfs(node.right)

def postorder_dfs(node):
    if node:
        postorder_dfs(node.left)
        postorder_dfs(node.right)
        print(node.data, end=' ')

print("In-Order DFS:   ", end='')
inorder_dfs(root)
print()

print("Pre-Order DFS:  ", end='')
preorder_dfs(root)
print()

print("Post-Order DFS: ", end='')
postorder_dfs(root)
print()