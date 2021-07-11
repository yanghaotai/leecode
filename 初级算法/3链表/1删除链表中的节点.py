'''
请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点。传入函数的唯一参数为 要被删除的节点 。

输入：head = [4,5,1,9], node = 5
输出：[4,1,9]

输入：head = [4,5,1,9], node = 1
输出：[4,5,9]
'''

def deleteNode(head,node):
    head.remove(node)
    return head

head = [4,5,1,9]
node = 5
print(deleteNode(head,node))
