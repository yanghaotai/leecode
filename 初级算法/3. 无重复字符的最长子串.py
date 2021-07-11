'''
https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。


'''


# a='abcdac'
# list = []
# for i in range(len(a)):
#     for j in range(len(a)-i):
#         list.append(a[j:i+j+1])
# print(list)
# list1 = {}
# for aa in list:
#     for i in aa:
#         flag = 1
#         if aa.count(i)>=2:
#             flag = 0
#             break
#     if(flag):
#         list1[aa]=len(aa)
# print(list1)
# print(max(list1.values()))
# max = max(list1.values())
# # print(list(list1.keys())[list(list1.values()).index(max(list1.values()))])
# # t = list(list1.keys())[list(list1.values()).index(max(list1.values()))]
# # print(t)
# m = {v:k for k, v in list1.items()}
# print(m)
# print(m[max])

def repeat(s):
        list = []
        list1 = []
        list2 = []

        # 取出所有的子字符串
        for i in range(len(s)):
            for j in range(len(s) - i):
                list.append(s[j:i + j + 1])

        # 过滤掉所有子字符串中有重复字符的子字符串
        for a in list:
            for i in a:
                flag = 1
                if a.count(i) >= 2:
                    flag = 0
                    break
            if (flag):
                list1.append(a)

        # 取出所有不重复子字符串中最长子串
        for i in list1:
            list2.append(len(i))
        return(list1,max(list2))

s1 = "abcabcbb"
print(repeat(s1))

s2 = "bbbbb"
print(repeat(s2))

s3 = "pwwkew"
print(repeat(s3))

# s4 = "pwke12 3 w"
# print(repeat(s4))

# list = []
# for i in range(len(s)):
#     for j in range(len(s) - i):
#         list.append(s[j:i + j + 1])
# print(list)

aa = [1,1,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3]
print(max(aa))