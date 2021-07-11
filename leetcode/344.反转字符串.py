'''
344. 反转字符串
难度 简单

编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。
不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。

示例 1：
输入：["h","e","l","l","o"]
输出：["o","l","l","e","h"]

示例 2：
输入：["H","a","n","n","a","h"]
输出：["h","a","n","n","a","H"]

'''

# 方法一
def reverseString(s):
    return s[::-1]

# 方法二
def reverseString1(s):
    s.reverse()
    return s

# 方法三
def reverseString2(s):
    return list(reversed(s))

# 方法三
def reverseString3(s):
    for i in range(len(s)//2):
        s[i],s[-1-i] = s[-i-1],s[i]
    return s


s1 = ["H","a","n","n","a","h"]
s2 = ["H","a","n","n","a","h"]
s3 = ["H","a","n","n","a","h"]
s4 = ["H","a","n","n","a","h","k"]
print(reverseString(s1))
print(reverseString1(s2))
print(reverseString2(s3))
print(reverseString3(s4))
