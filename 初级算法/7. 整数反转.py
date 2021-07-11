'''
https://leetcode-cn.com/problems/reverse-integer/
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321

 示例 2:

输入: -123
输出: -321

示例 3:

输入: 120
输出: 21

注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

'''

def reverse(s):
    # 判断是否是整数
    if isinstance(s,int):
        # 判断是否溢出
        if (s>(2**31 - 1))or(s < - 2**31):
            return 0
        # 循环处理末尾为0的情况
        while s % 10 == 0:
            s = s // 10
        # 将整数转化为字符串后反转
        if s>=0:
            s = str(s)[::-1]
        else:
            s = '-'+str(-s)[::-1]
        return int(s)
    else:
        return('非整数')

s1 = 123
print(s1,reverse(s1))

s2 = -123
print(s2,reverse(s2))

s3 = 120
print(s3,reverse(s3))

s4 = 120
print(s4,reverse(s4),type(reverse(s4)))


# s = -12300
# while s % 10 == 0:
#     s = s//10
# print(s)