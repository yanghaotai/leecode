'''
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1

s = "leetcode"
返回 0

s = "loveleetcode"
返回 2
'''


# 方法一
# 统计到字符个数为1的字符，返回索引，未找到返回-1
def firstUniqChar(s):
    for i in range(len(s)):
        if s.count(s[i]) == 1:
            return i
    else:
        return -1

# 方法二
## 使用 find 和 rfind
def firstUniqChar1(s):
    for x in s:
        if s.find(x) == s.rfind(x):
            return s.find(x)
    return -1

s = 'leetcode'
s1 = 'loveleetcode'
s2 = 'abcdabcd'
print(firstUniqChar(s))
print(firstUniqChar(s1))
print(firstUniqChar(s2))
print(firstUniqChar1(s))
print(firstUniqChar1(s1))
print(firstUniqChar1(s2))

ss = 'sdfdsf'
sss = []
for i in range(len(ss)):
    sss.append(ss[i])
print(sss)