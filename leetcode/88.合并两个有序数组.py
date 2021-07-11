'''
88. 合并两个有序数组
难度 简单

给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。你可以假设 nums1 的空间大小等于 m + n，这样它就有足够的空间保存来自 nums2 的元素。

示例 1：
输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]

示例 2：
输入：nums1 = [1], m = 1, nums2 = [], n = 0
输出：[1]

'''


def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """

    # l为nums1的m开始索引, r为nums2的n开始索引，index为修改nums1的开始索引，然后从nums1末尾开始往前遍历
    l, r, index = m - 1, n - 1, len(nums1) - 1
    # 按从大到小，从后往前修改nums1的值，每次都赋值为nums1和nums2的当前索引的较大值，然后移动索引
    while l >= 0 and r >= 0:
        # 如果nums1[l] >= nums2[r]，则先赋值为nums1[l]，l索引减少
        if nums1[l] >= nums2[r]:
            nums1[index] = nums1[l]
            l -= 1
        else:
            # 如果nums1[l] <= nums2[r]，则先赋值为nums2[r]，r索引减少
            nums1[index] = nums2[r]
            r -= 1
        # 当前nums1修改索引减少1
        index -= 1
    # nums2没有遍历完n个，则继续遍历，直到n个完成
    while r >= 0:
        nums1[index] = nums2[r]
        r -= 1
        index -= 1
    '''
    这里大家疑惑如果nums1没有遍历完m个即l >= 0，为何不继续遍历，因为没有必要了，因为修改的就是nums1,
    他的最后剩下的前l个本身就是有序的了，所以不用继续操作
    '''

    return nums1

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
print(merge(nums1, m, nums2, n))