'''
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

输入: s = "anagram", t = "nagaram"
输出: true

输入: s = "rat", t = "car"
输出: false
'''

# 方法一
# 将两个字符串切片转换成list，再排序，比较是否相等
def isAnagram(s, t):
    s1 = []
    t1 = []
    for i in range(len(s)):
        s1.append(s[i])
    for j in range(len(t)):
        t1.append(t[j])
    s1.sort()
    t1.sort()
    if s1 == t1:
        return True
    else:
        return False

# 方法二
# 将字符串排序，然后比对字符串是否相等
# 内置函数sorted()可以对字符串排序
def isAnagram1(s, t):
    return sorted(s) == sorted(t)

# 方法三
# 使用 collections.Counter 将字符串转换为 hashmap 格式
import collections
def isAnagram2(s, t):
    return collections.Counter(s) == collections.Counter(t)


s = "anagram"
t = "nagaram"
print(isAnagram(s,t))
print(isAnagram1(s,t))
print(isAnagram2(s,t))

