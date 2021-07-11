'''
6. Z 字形变换
难度 中等

将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
比如输入字符串为 "PAYPALISHIRING"行数为 3 时，排列如下：
P   A   H   N
A P L S I I G
Y   I   R
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。
请你实现这个将字符串进行指定行数变换的函数：
string convert(string s, int numRows);

示例 1：
输入：s = "PAYPALISHIRING", numRows = 3
输出："PAHNAPLSIIGYIR"

示例 2：
输入：s = "PAYPALISHIRING", numRows = 4
输出："PINALSIGYAHRPI"
解释：
P     I    N
A   L S  I G
Y A   H R
P     I

示例 3：
输入：s = "A", numRows = 1
输出："A"
'''

'''
思路
对列来说，一直往右走，
对行来说，碰到边界就改变方向；
'''
def convert(s,num):
    if num>1:
        # 存储找到的元素
        # 注意不能[[]] * n 这样复制的id相同
        list1 = [[] for i in range(num)]
        # 从矩阵中找
        array = [s for i in range(num)]
        # flag 碰到边界就改变方向
        i,flag = 0,1
        for j in range(len(s)):
            list1[i].append(array[i][j])
            i += flag
            if i==0 or i==num-1:
                flag *= -1
        list2 = []
        for i in list1:
            list2.extend(i)
        return ''.join(list2)
    else:
        return s

s = "PAYPALI"
num = 3
print(convert(s,num))
