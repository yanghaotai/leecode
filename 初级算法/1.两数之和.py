'''
https://leetcode-cn.com/problems/two-sum/

给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]


'''


def sum(nums,target):
    s = []
    for i in range(len(nums)):
        for j in range(len(nums)-1,0,-1):
            if (nums[i] + nums[j] == target) and i!=j:
                s.append([i,j])
            if i==j:
                break
    return(s)

nums = [2, 7, 11, 15]
target = 9
print(nums,sum(nums,target))

nums1 = [1,3,4,2]
target1 = 6
print(nums1,sum(nums1,target1),len(sum(nums1,target1)))
