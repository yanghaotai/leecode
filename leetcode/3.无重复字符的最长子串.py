'''
3. 无重复字符的最长子串
难度 中等

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


# 暴力法 取出所有子字符串，过滤掉重复子字符串，返回最长的子串长度
def repeat(s):
        list = []
        list1 = []
        list2 = []

        # 取出所有的子字符串
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                list.append(s[i:j])
        print(list)

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

def lengthOfLongestSubstring(s):
    # 哈希集合，记录每个字符是否出现过
    occ = set()
    n = len(s)
    # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
    rk, ans = -1, 0
    for i in range(n):
        if i != 0:
            # 左指针向右移动一格，移除一个字符
            occ.remove(s[i - 1])
        while rk + 1 < n and s[rk + 1] not in occ:
            # 不断地移动右指针
            occ.add(s[rk + 1])
            rk += 1
        # 第 i 到 rk 个字符是一个极长的无重复字符子串
        ans = max(ans, rk - i + 1)
    return ans


s1 = "abcabcbb"
print(repeat(s1))
print(lengthOfLongestSubstring(s1))

s2 = "bbbbb"
print(repeat(s2))
print(lengthOfLongestSubstring(s2))

s3 = "pwwkew"
print(repeat(s3))
print(lengthOfLongestSubstring(s3))

