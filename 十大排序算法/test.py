# 冒泡排序  比较相邻两个数
def bubble(lis):
    for i in range(1,len(lis)):
        for j in range(len(lis)-i):
            if lis[j] > lis[j+1]:
                lis[j],lis[j+1]=lis[j+1],lis[j]
    return lis


# 快速排序 选择一个基准 递归实现
def quick(lis):
    lis1 = [[],[],[]]
    q = lis[-1]  # 基准数，第一个或者最后一个
    for i in lis:
        if i < q:  # 小于基准放左边
            lis1[0].append(i)
        elif i > q:  # 大于基准放右边
            lis1[2].append(i)
        else:  # 等于基准放中间
            lis1[1].append(i)

    if len(lis1[0]) > 1:  # 小于基准部分 递归
        lis1[0] = quick(lis1[0])

    if len(lis1[2]) > 1:  # 大于基准部分 递归
        lis1[2] = quick(lis1[2])


    lis1[0].extend(lis1[1])
    lis1[0].extend(lis1[2])

    return lis1[0]

# 插入排序
# 将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列。
# 从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置。（如果待插入的元素与有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面。）
def insert_sort(lis):
    lis1 = [lis[0]]
    for i in lis[1:]:
        flag = 1
        for j in range(len(lis1)-1,-1,-1):
            if i >= lis1[j]:
                lis1.insert(j+1,i)
                flag = 0
                break
        if flag:
            lis1.insert(0,i)

    return lis1

def insert_sort1(lis):
    for i in range(1,len(lis)):
        key = lis[i]
        j = i -1
        while j >= 0 and key < lis[j]:
            lis[j+1] = lis[j]
            j -= 1
        lis[j+1] = key

    return lis

# 希尔排序
# 希尔排序的基本思想是：先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，待整个序列中的记录“基本有序”时，再对全体记录进行依次直接插入排序。
def shell_sort(lis):
    group = int(len(lis)/2)
    while group > 0:
        for i in range(len(lis)):
            key = lis[i]
            j = i
            while j >= group and key < lis[j - group]:
                lis[j] = lis[j - group]
                j -= group
            lis[j] = key
        group = int(group/2)

    return lis

# 选择排序
# 首先在未排序序列中找到最小元素，存放到排序序列的起始位置
# 再从剩余未排序元素中继续寻找最小元素，然后放到已排序序列的末尾。
def select_sort(lis):
    for i in range(len(lis)-1):
        mi = i
        for j in range(i+1,len(lis)):
            if lis[j] < lis[mi]:
                mi = j

        if mi != i:
            lis[i],lis[mi] = lis[mi],lis[i]

    return lis

# 堆排序  没看懂
# 堆排序（Heapsort）是指利用堆这种数据结构所设计的一种排序算法。堆积是一个近似完全二叉树的结构，并同时满足堆积的性质：即子结点的键值或索引总是小于（或者大于）它的父节点。堆排序可以说是一种利用堆的概念来排序的选择排序。分为两种方法：
# 大顶堆：每个节点的值都大于或等于其子节点的值，在堆排序算法中用于升序排列；
# 小顶堆：每个节点的值都小于或等于其子节点的值，在堆排序算法中用于降序排列；
# 堆排序的平均时间复杂度为 Ο(nlogn)。
def heapify(arr,n,i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr,n,largest)

def heapSort(arr):
    n = len(arr)

    for i in range(n,-1,-1):
        heapify(arr,n,i)

    for i in range(n-1,0,-1):
        arr[i],arr[0] = arr[0],arr[i]
        heapify(arr,i,0)

    return arr

# 归并排序 分治法-2-4-8插入排序
def merge_sort(lis):
    n = int(len(lis)/2)
    lis0 = lis[:n]
    lis1 = lis[n:]

    if len(lis0) > 1:
        lis0 = merge_sort(lis0)

    if len(lis1) > 1:
        lis1 = merge_sort(lis1)

    for i in range(len(lis1)):
        flag = 1
        for j in range(len(lis0)):
            if lis1[i] < lis0[j]:
                flag = 0
                lis0.insert(j,lis1[i])
                break

        if flag == 1:
            lis0.extend(lis1[i:])
            break


    return lis0

# 计数排序 字典计数-还原
def countSort(lis):
    lis1 = {}
    for i in set(lis):
        lis1[i] = lis.count(i)

    lis2 = []
    for i in range(min(lis1.keys()),max(lis1.keys())+1):
        if i in lis1.keys():
            for j in range(lis1[i]):
                lis2.append(i)

    return lis2

# 桶排序
# 桶排序是计数排序的升级版
def bucket_sort(lis):
    mi = min(lis)
    ma = max(lis)

    #桶大小
    t = (ma-mi)/len(lis)

    # 桶数组
    lis1 = [[] for _ in range(len(lis)+1)]

    for i in lis:
        lis1[int((i-mi)//t)].append(i)

    # 回填
    lis2 = []
    for i in range(len(lis1)):
        for j in sorted(lis1[i]):
            lis2.append(j)

    return lis2

# 基数排序
# 基数排序是一种非比较型整数排序算法，其原理是将整数按位数切割成不同的数字，然后按每个位数分别比较。由于整数也可以表达字符串（比如名字或日期）和特定格式的浮点数，所以基数排序也不是只能使用于整数。
# 基数排序：根据键值的每位数字来分配桶；
def radix_sort(lis):
    ma = max(lis)
    num = 1
    while ma > 10 ** num:
        num += 1

    for i in range(num):
        li = [[] for _ in range(10)]
        for data in lis:
            index = int(data/(10**i)%10)
            li[index].append(data)

        j = 0
        for k in range(10):
            for data in li[k]:
                lis[j] = data
                j += 1

    return lis


lis1 = [1,4,3,5,2,6,43,45,323,23,13,2,4,223,34]
lis2 = [1,4,3,5,2,6,43,45,323,23,13,2,4,223,34]
lis3 = [1,4,3,5,2,6,43,45,323,23,13,2,4,223,34]
lis4 = [1,4,3,5,2,6,43,45,323,23,13,2,4,223,34]
lis5 = [1,4,3,5,2,6,43,45,323,23,13,2,4,223,34]
lis6 = [1,4,3,5,2,6,43,45,323,23,13,2,4,223,34]
lis7 = [1,4,3,5,2,6,43,45,323,23,13,2,4,223,34]
lis8 = [1,4,3,5,2,6,43,45,323,23,13,2,4,223,34]
lis9 = [1,4,3,5,2,6,43,45,323,23,13,2,4,223,34]
lis10 = [1,4,3,5,2,6,43,45,323,23,13,2,4,223,34]
lis11 = [1,4,3,5,2,6,43,45,323,23,13,2,4,223,34]
print(bubble(lis1))
print(quick(lis2))
print(insert_sort(lis3))
print(insert_sort1(lis4))
print(shell_sort(lis5))
print(select_sort(lis6))
print(heapSort(lis7))
print(merge_sort(lis8))
print(countSort(lis9))
print(bucket_sort(lis10))
print(radix_sort(lis11))