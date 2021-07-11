'''
557. 反转字符串中的单词 III
难度 简单

给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

示例：
输入："Let's take LeetCode contest"
输出："s'teL ekat edoCteeL tsetnoc"

提示：
在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。
'''


def reverseWords(s: str) -> str:
    s1 = s.split(' ')
    s2 = []
    for i in s1:
        s2.append(i[::-1])
    return ' '.join(s2)

s = "Let's take LeetCode contest"
print(reverseWords(s))