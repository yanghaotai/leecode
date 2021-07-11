'''
8、计数排序
计数排序的核心在于将输入的数据值转化为键存储在额外开辟的数组空间中。作为一种线性时间复杂度的排序，计数排序要求输入的数据必须是有确定范围的整数。
'''

# 方法一：
def countSort(lis):
    mi = 0
    ma = 0

    for i in lis:
        if mi > i:
            mi = i
        if ma < i:
            ma = i

    lis1 = {}
    for i in lis:
        if i in lis1.keys():
            lis1[i] += 1
        else:
            lis1[i] = 1


    lis2 = []
    for i in range(mi,ma+1):
        if i in lis1.keys():
            for j in range(lis1[i]):
                lis2.append(i)

    return lis2

# 方法二：
def countSort1(lis):
    lis1 = {}
    for i in set(lis):
        lis1[i] = lis.count(i)

    lis2 = []
    for i in range(min(lis1.keys()),max(lis1.keys())+1):
        if i in lis1.keys():
            for j in range(lis1[i]):
                lis2.append(i)

    return lis2


arr = [2,1,32,41,42,33,4545,0,343,434,34232,44,3434,43,543,48,5]
arr1 = [2,1,32,41,42,33,4545,0,343,434,34232,44,3434,43,543,48,5]
print(countSort(arr))
print(countSort1(arr1))