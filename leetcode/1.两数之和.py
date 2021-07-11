'''
1. 两数之和
难度 简单

给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回它们的数组下标。
    你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
    你可以按任意顺序返回答案。

示例 ：
    输入：nums = [2,7,11,15], target = 9
    输出：[0,1]
    解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

本题可以通过三种方式去解答
    暴力法1:双层for循环进行遍历，属于最基础的检索与判断方式O(n*n)
    暴力法2:通过python的**str in list**方式逐个遍历，虽然代码看似简单，但每一次in操作的复杂度一样是O(n),所以总体复杂度O(n*n)
    之所以把这道题归档在HashMap类中，是因为通过HashMap的方式，能在O(n)的时间复杂度下完成

'''


def twoSum1(nums, target):
    for i in range(len(nums) - 1):
        base = nums[i]
        for j in range(i + 1, len(nums)):
            if base + nums[j] == target:
                return [i, j]



def twoSum2(nums, target):
    for i in range(len(nums) - 1):
        base = nums[i]
        other = target - base
        if other in nums[i + 1:]:
             # 这里注意index设置start，避免出现target = 6，[3,3]返回[0,0]的错误
            return [i, nums.index(other, i + 1)]


def twoSum3(nums, target):
    tmp = {}
    for k, v in enumerate(nums):
        if target - v in tmp:
            return [tmp[target - v], k]
        tmp[v] = k


nums = [2,7,11,15]
target = 9
print(twoSum1(nums,target))
print(twoSum2(nums,target))
print(twoSum3(nums,target))

