'''
3、插入排序
插入排序的代码实现虽然没有冒泡排序和选择排序那么简单粗暴，但它的原理应该是最容易理解的了，因为只要打过扑克牌的人都应该能够秒懂。插入排序是一种最简单直观的排序算法，它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
插入排序和冒泡排序一样，也有一种优化算法，叫做拆半插入。
（1）算法步骤
将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列。
从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置。（如果待插入的元素与有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面。）
'''

# 方法一
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# 方法二
def direct_insertion_sort(d):
 d1 = [d[0]]
 for i in d[1:]:
     state = 1
     for j in range(len(d1) - 1, -1, -1):
         if i >= d1[j]:  # 找到大于等于已排序
             d1.insert(j + 1, i)  # 将元素插入数组
             state = 0
             break
     if state:  # d1元素全部大于i，插入数组最前面
         d1.insert(0, i)
 return d1

arr = [2,1,32,42,42,32,4545,0,343,434,34232,44,3434,43,543,42]
print(insertionSort(arr))
print(direct_insertion_sort(arr))
