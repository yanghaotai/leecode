'''
https://leetcode-cn.com/problems/longest-palindromic-substring/
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。

示例 2：

输入: "cbbd"
输出: "bb"


'''

def huiwen(s):
    list = []
    list1 = []
    list2 = []
    # 取出所有的子字符串(大于1个字符)
    for i in range(1,len(s)):
        for j in range(len(s)-i):
            list.append(s[j:i+j+1])
    # 判断子串是否是回文
    for i in list:
        if i==i[::-1]:
            list1.append([i,len(i)])
            list2.append(len(i))
    # 取最大的回文子串(备注：缺陷在于存在多个最大回文子串时只取了一个)
    if list1:
        t = list1[list2.index(max(list2))]
        return t
    else:
        return('没有回文子串')

s = 'babad'
print(huiwen(s))

s1 = 'cbbd'
print(huiwen(s1))


def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    sum = 0
    for i in range(len(s)):
        if s[i] == 'I':
            a = 1
            try:
                if(s[i + 1] == 'V' or s[i + 1] == 'X'):
                    a = -1
            except:
                pass
        elif s[i] == 'V':
            a = 5
        elif s[i] == 'X':
            a = 10
            try:
                if(s[i + 1] == 'L' or s[i + 1] == 'C'):
                    a = -10
            except:
                pass
        elif s[i] == 'L':
            a = 50
        elif s[i] == 'C':
            a = 100
            try:
                if(s[i + 1] == 'D' or s[i + 1] == 'M'):
                    a = -100
            except:
                pass
        elif s[i] == 'D':
            a = 500
        elif s[i] == 'M':
            a = 1000
        sum += a
    return sum
print(romanToInt('IV'))

# try:
#     1 > 2
# except:
#     print('++++')
#     a = 1
# else:
#     a = -1
# print(a)