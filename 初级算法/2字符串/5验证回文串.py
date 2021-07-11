'''
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。

输入: "A man, a plan, a canal: Panama"
输出: true

输入: "race a car"
输出: false
'''

# 方法一
# 将字符串转换成大写或者小写,将字母或者数字加到列表中，正反排序进行比较
def isPalindrome(s):
    s1 = []
    s = s.upper()
    # s = s.lower()
    for i in s:
        if i.isalnum():
            s1.append(i)
    if s1 == s1[::-1]:
        return True
    else:
        return False

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))


tt = 'd'
print(tt.isdigit())