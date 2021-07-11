'''
189. 旋转数组
难度 中等

给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

进阶：
尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
你可以使用空间复杂度为 O(1) 的 原地 算法解决这个问题吗？

示例 1:
输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]

示例2:
输入：nums = [-1,-100,3,99], k = 2
输出：[3,99,-1,-100]
解释:
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]。
'''


def rotate(nums, k) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    print(id(nums))
    for i in range(k):
        nums.insert(0, nums[-1])
        nums.pop()
    print(id(nums))
    return nums

def rotate1(nums, k) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    l = len(nums)
    return nums[l-k:]+nums[:l-k]

nums1 = [1,2,3,4,5,6,7]
k1 = 3

nums2 = [-1,-100,3,99]
k2 = 2

nums3 = [1,2,3,4,5,6,7]
k3 = 3

nums4 = [-1,-100,3,99]
k4 = 2

print(rotate(nums1, k1))
print(rotate(nums2, k2))
print(rotate1(nums3, k3))
print(rotate1(nums4, k4))