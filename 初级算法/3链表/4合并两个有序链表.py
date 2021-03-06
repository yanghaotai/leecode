'''
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]

输入：l1 = [], l2 = []
输出：[]

输入：l1 = [], l2 = [0]
输出：[0]
'''


'''
append()    在列表的末尾添加一个元素    
extend()    在列表的末尾至少添加一个元素    
insert()    在列表的任意位置添加一个元素    
'''
def mergeTwoLists(l1, l2):
    l1.extend(l2)
    l1.sort()
    return l1

l1 = [1,2,4]
l2 = [1,3,4]
print(mergeTwoLists(l1,l2))