'''
请判断一个链表是否为回文链表。

输入: 1->2
输出: false

输入: 1->2->2->1
输出: true
'''

def isPalindrome(head):
    list = head.split('->')
    if list == list[::-1]:
        return True
    else:
        return False

head = '1->2->2->1'
print(isPalindrome(head))

