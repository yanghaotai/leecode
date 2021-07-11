'''
5. 最长回文子串
难度 中等

给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。

示例 2：
输入: "cbbd"
输出: "bb"

示例 3：
输入：s = "a"
输出："a"

示例 4：
输入：s = "ac"
输出："a"
'''

def huiwen(s):
    list = []
    list1 = []
    list2 = []

    # 取出所有的子字符串(大于1个字符)
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            list.append(s[i:j])

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

