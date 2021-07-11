'''
请你来实现一个myAtoi(string s)函数，使其能将字符串转换成一个 32 位有符号整数（类似 C/C++ 中的 atoi 函数）。

函数myAtoi(string s) 的算法如下：

读入字符串并丢弃无用的前导空格
检查下一个字符（假设还未到字符末尾）为正还是负号，读取该字符（如果有）。 确定最终结果是负数还是正数。 如果两者都不存在，则假定结果为正。
读入下一个字符，直到到达下一个非数字字符或到达输入的结尾。字符串的其余部分将被忽略。
将前面步骤读入的这些数字转换为整数（即，"123" -> 123， "0032" -> 32）。如果没有读入数字，则整数为 0 。必要时更改符号（从步骤 2 开始）。
如果整数数超过 32 位有符号整数范围 [−2**31,2**31− 1] ，需要截断这个整数，使其保持在这个范围内。具体来说，小于 −2**31 的整数应该被固定为 −2**31 ，大于 2**31− 1 的整数应该被固定为 2**31− 1 。
返回整数作为最终结果。
注意：

本题中的空白字符只包括空格字符 ' ' 。
除前导空格或数字后的其余字符串外，请勿忽略 任何其他字符。


输入：s = "42"
输出：42

输入：s = "   -42"
输出：-42

输入：s = "4193 with words"
输出：4193

输入：s = "words and 987"
输出：0

输入：s = "-91283472332"
输出：-2147483648
'''

import re
def myAtoi(s):
    s = s.strip(" ")  # 去除前端空格
    pattern = r'[+|-]?[0-9]+'  # 正则表达，检查正负号有无以及是否为数字
    news = re.match(pattern, s)
    if not news:
        return 0
    else:
        nums = int(news.group())
        if nums <= -2 ** 31:
            return -2 ** 31
        elif nums >= 2 ** 31 - 1:
            return 2 ** 31 - 1
        else:
            return nums


s = "4193 with words"
print(myAtoi(s))