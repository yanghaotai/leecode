'''
53. 最大子序和
难度 简单

给定一个整数数组 nums，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例 1：
输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组[4,-1,2,1] 的和最大，为6 。

示例 2：
输入：nums = [1]
输出：1

示例 3：
输入：nums = [0]
输出：0

示例 4：
输入：nums = [-1]
输出：-1

示例 5：
输入：nums = [-100000]
输出：-100000

'''

def maxSubArray(nums):
    list1 = []
    list2 = []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)+1):
            list1.append(nums[i:j])
    for i in list1:
        list2.append(sum(i))

    return max(list2)


def maxSubArray1(nums):
    tmp = nums[0]
    max_ = tmp
    n = len(nums)
    for i in range(1, n):
        # 当前序列加上此时的元素的值大于tmp的值，说明最大序列和可能出现在后续序列中，记录此时的最大值
        if tmp + nums[i] > nums[i]:
            max_ = max(max_, tmp + nums[i])
            tmp = tmp + nums[i]
        else:
            # 当tmp(当前和)小于下一个元素时，当前最长序列到此为止。以该元素为起点继续找最大子序列,
            # 并记录此时的最大值
            max_ = max(max_, nums[i])
            tmp = nums[i]
    return max_


nums1 = [-2,1,-3,4,-1,2,1,-5,4]
nums2 = [1,334,2]
nums3 = [0]
nums4 = [-1]
nums5 = [-100000]
print(maxSubArray(nums1))
print(maxSubArray(nums2))
print(maxSubArray(nums3))
print(maxSubArray(nums4))
print(maxSubArray(nums5))
print(maxSubArray1(nums1))
print(maxSubArray1(nums2))
print(maxSubArray1(nums3))
print(maxSubArray1(nums4))
print(maxSubArray1(nums5))