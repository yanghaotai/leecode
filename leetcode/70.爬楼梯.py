'''
70. 爬楼梯
难度 简单

假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。

示例 1：
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶

示例 2：
输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
'''

from functools import lru_cache
@lru_cache
def climbStairs(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2
    # 类似斐波那数列
    return climbStairs(n - 1) + climbStairs(n - 2)


def climbStairs1(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2
    # 类似斐波那数列
    a,b,tmp=1,2,0
    i = 2
    while i < n:
        tmp = a + b
        a,b = b,tmp
        i += 1
    return tmp


print(climbStairs(5))
print(climbStairs1(5))