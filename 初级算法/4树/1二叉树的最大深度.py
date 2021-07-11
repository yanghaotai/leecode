'''
给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，
    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度3 。

'''

def maxDepth(root):
    if root is None:
        return 0
    temp = list()
    temp.append(root)
    res = 0
    while len(temp):
        size = len(temp)
        while size > 0:
            node = temp[0]
            del temp[0]
            if node.left is not None:
                temp.append(node.left)
            if node.right is not None:
                temp.append(node.right)
            size = size - 1
        res = res + 1
    return res

root = [3,9,20,'','',15,7]
print(maxDepth(root))