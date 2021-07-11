'''
1137. 第 N 个泰波那契数
难度 简单

泰波那契序列 Tn 定义如下：
T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2
给你整数 n，请返回第 n 个泰波那契数 Tn 的值。

示例 1：
输入：n = 4
输出：4
解释：
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
示例 2：
输入：n = 25
输出：1389537
'''

from functools import lru_cache
@lru_cache(None)
def tribonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return tribonacci(n-3) + tribonacci(n-2) + tribonacci(n-1)

def tribonacci1(n: int) -> int:
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    a,b,c = 0,1,1
    while n > 2:
        res = a + b + c
        a,b,c = b,c,res
        n -= 1
    return res


print(tribonacci(10))
print(tribonacci1(10))