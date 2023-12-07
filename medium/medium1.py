class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildBST(nums):
    if not nums:
        return None

    root = TreeNode(nums[0])

    for num in nums[1:]:
        insertIntoBST(root, num)

    return root

def insertIntoBST(root, val):
    if not root:
        return TreeNode(val)

    if val < root.val:
        root.left = insertIntoBST(root.left, val)
    elif val > root.val:
        root.right = insertIntoBST(root.right, val)

    return root

def lowestCommonAncestor(root, p, q):
    if not root or root.val == p.val or root.val == q.val:
        return root

    left_lca = lowestCommonAncestor(root.left, p, q)
    right_lca = lowestCommonAncestor(root.right, p, q)

    if left_lca and right_lca:
        return root

    return left_lca if left_lca else right_lca

nums = list(map(int, input("Enter the values of BST nodes separated by space: ").split()))

p_val = int(input("Enter the value of node p: "))
q_val = int(input("Enter the value of node q: "))

root = buildBST(nums)

p = TreeNode(p_val)
q = TreeNode(q_val)

lca = lowestCommonAncestor(root, p, q)
print(f"The lowest common ancestor of nodes {p.val} and {q.val} is {lca.val}")
