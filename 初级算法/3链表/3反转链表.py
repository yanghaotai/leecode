'''
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]

输入：head = [1,2]
输出：[2,1]

输入：head = []
输出：[]
'''

# 方法一
def reverseList(head):
    return head[::-1]

# 方法二
def reverseList1(head):
    head.reverse()
    return head

# 方法三
def reverseList2(head):
    reversed(head)
    return head

head = [1,2,3,4,5]
print(reverseList(head))
print(reverseList1(head))
print(reverseList2(head))