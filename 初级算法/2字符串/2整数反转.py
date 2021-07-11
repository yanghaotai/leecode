'''
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。

如果反转后整数超过 32 位的有符号整数的范围[−2**31,2**32− 1] ，就返回 0。

假设环境不允许存储 64 位整数（有符号或无符号）。

输入：x = 123
输出：321

输入：x = -123
输出：-321

输入：x = 120
输出：21

输入：x = 0
输出：0

'''

# 方法一
# 暴力破解，数字转字符串，处理范围
def reverse(x):
    # 将x先转成绝对值正数，之后转成字符串，再切片反转
    s = str(abs(x))[::-1]
    # 处理范围
    if int(s) > 2**31-1 or int(s) < 2**31*-1:
        return 0
    # 处理负数情况
    return int(s) if x > 0 else int(s)*-1

# 方法二
def reverse1(x):
    n = 0
    if x > 0:
        l = 1
    else:
        l = -1
    x = abs(x)
    while abs(x)>=1:
        n = n*10 + x%10
        x = x//10
    if -2**31<=n*l<=2**31-1:
        return n*l
    return 0

x = 123
x1 = -123
x2 = 120
x3 = 0
print(reverse(x))
print(reverse(x1))
print(reverse(x2))
print(reverse(x3))
print(reverse1(x))
print(reverse1(x1))
print(reverse1(x2))
print(reverse1(x3))