'''
给定一个正整数 n ，输出外观数列的第 n 项。
「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。

你可以将其视作是由递归公式定义的数字字符串序列：
countAndSay(1) = "1"
countAndSay(n) 是对 countAndSay(n-1) 的描述，然后转换成另一个数字字符串。

前五项如下：
1.     1
2.     11
3.     21
4.     1211
5.     111221
第一项是数字 1
描述前一项，这个数是 1 即 “ 一 个 1 ”，记作 "11"
描述前一项，这个数是 11 即 “ 二 个 1 ” ，记作 "21"
描述前一项，这个数是 21 即 “ 一 个 2 + 一 个 1 ” ，记作 "1211"
描述前一项，这个数是 1211 即 “ 一 个 1 + 一 个 2 + 二 个 1 ” ，记作 "111221"

输入：n = 1
输出："1"

输入：n = 5
输出："111221"
解释：
countAndSay(1) = "1"
countAndSay(2) = 读 "1" = 一 个 1 = "11"
countAndSay(3) = 读 "11" = 二 个 1 = "21"
countAndSay(4) = 读 "21" = 一 个 2 + 一 个 1 = "12" + "11" = "1211"
countAndSay(5) = 读 "1211" = 一 个 1 + 一 个 2 + 两 个 1= "11" + "12" + "21" = "111221"
'''


## 递归 + 双指针
def countAndSay(n):
    if n == 1:
        return '1'
    s = countAndSay(n - 1)

    ans = ''
    start, end = 0, 0
    while end < len(s):
        while end < len(s) and s[start] == s[end]:
            end += 1
        ans += str(end - start) + s[start]
        start = end

    return ans

n = 5
print(countAndSay(n))
