# A Binary Tree stored as a simple list (array)
# Index 0 = root
# For any node at index i:
#   Left child  → (2 * i) + 1
#   Right child → (2 * i) + 2

# Initialize empty tree
tree_size = 10
tree      = [None] * tree_size


# Set the root node (always at index 0)
def set_root(key):
    tree[0] = key


# Set left child of a parent
def set_left(parent_index, key):
    left_index = (2 * parent_index) + 1

    if tree[parent_index] is None:
        print(f"Error: No parent at index {parent_index}")
    elif left_index >= tree_size:
        print("Error: Tree is full")
    else:
        tree[left_index] = key
        print(f"Set '{key}' as left child of '{tree[parent_index]}'")


# Set right child of a parent
def set_right(parent_index, key):
    right_index = (2 * parent_index) + 2

    if tree[parent_index] is None:
        print(f"Error: No parent at index {parent_index}")
    elif right_index >= tree_size:
        print("Error: Tree is full")
    else:
        tree[right_index] = key
        print(f"Set '{key}' as right child of '{tree[parent_index]}'")


# Display the tree as an array
def display_array():
    print("\nTree as array:")
    for i in range(tree_size):
        print(f"  Index {i} → {tree[i]}")


# Display the tree in a readable shape
def display_tree():
    print("\nTree structure:")
    if tree[0] is None:
        print("  Tree is empty")
        return

    # Level 0 — root
    print(f"         {tree[0] or '_'}")

    # Level 1 — index 1 and 2
    left  = tree[1] if tree[1] is not None else '_'
    right = tree[2] if tree[2] is not None else '_'
    print(f"       /   \\")
    print(f"      {left}     {right}")

    # Level 2 — index 3, 4, 5, 6
    ll = tree[3] if tree[3] is not None else '_'
    lr = tree[4] if tree[4] is not None else '_'
    rl = tree[5] if tree[5] is not None else '_'
    rr = tree[6] if tree[6] is not None else '_'
    print(f"     / \\   / \\")
    print(f"    {ll}   {lr} {rl}   {rr}")


# ─── Build the tree ───

set_root('A')           # index 0  →  root

set_left(0,  'B')       # index 1  →  left  child of A
set_right(0, 'C')       # index 2  →  right child of A

set_left(1,  'D')       # index 3  →  left  child of B
set_right(1, 'E')       # index 4  →  right child of B

# ─── Output ───
display_tree()
display_array()