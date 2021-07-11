'''
283. 移动零
难度 简单

给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]

说明:
必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
'''

# 双指针
def moveZeroes(nums:list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    s = 0
    f = 0
    while f < len(nums):
        if nums[f] != 0:
            nums[s], nums[f] = nums[f], nums[s]
            s += 1
        f += 1
    return nums

nums = [0,1,0,3,12]
print(moveZeroes(nums))