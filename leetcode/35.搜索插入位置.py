'''
35. 搜索插入位置
难度 简单

给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
你可以假设数组中无重复元素。

示例 1:
输入: [1,3,5,6], 5
输出: 2

示例2:
输入: [1,3,5,6], 2
输出: 1

示例 3:
输入: [1,3,5,6], 7
输出: 4

示例 4:
输入: [1,3,5,6], 0
输出: 0
'''

def searchInsert(nums, target):
    nums.append(target)
    nums.sort()
    return nums.index(target)

def searchInsert1(nums, target):
    low,high = 0,len(nums)-1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid -1

    if nums[mid] > target: #注意，是target替换nums[mid]的位置
        return mid

    return mid + 1


nums = [1,3,5,6]
trget = 2
print(searchInsert(nums, trget))

nums1 = [1,3,5,6]
trget = 7
print(searchInsert1(nums1, trget))
