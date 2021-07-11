'''
4. 寻找两个正序数组的中位数
难度 困难

给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

示例 1：
输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2

示例 2：
输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5

示例 3：
输入：nums1 = [0,0], nums2 = [0,0]
输出：0.00000

示例 4：
输入：nums1 = [], nums2 = [1]
输出：1.00000

示例 5：
输入：nums1 = [2], nums2 = []
输出：2.00000

'''

def find(nums1,nums2):
    for i in nums2:
        nums1.append(i)
    nums1.sort()
    index = len(nums1)//2
    if len(nums1) == 0:
        return 0
    if len(nums1)%2:
        return nums1[index]
    else:
        return (nums1[index-1]+nums1[index])/2

nums1 = []
nums2 = []
print(find(nums1, nums2))