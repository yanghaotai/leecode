'''
930. 和相同的二元子数组
难度 中等

给你一个二元数组 nums ，和一个整数 goal ，请你统计并返回有多少个和为 goal 的 非空 子数组。
子数组 是数组的一段连续部分。

示例 1：
输入：nums = [1,0,1,0,1], goal = 2
输出：4
解释：
如下面黑体所示，有 4 个满足题目要求的子数组：
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]

示例 2：
输入：nums = [0,0,0,0,0], goal = 0
输出：15
'''


def numSubarraysWithSum(nums, goal):
    li = []
    sum1 = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            li.append(nums[i:j])
    for i in li:
        if sum(i) == goal:
            sum1 += 1
    return sum1

nums = [0,0,0,0,0]
goal = 0
print(numSubarraysWithSum(nums, goal))