'''
10、基数排序
基数排序是一种非比较型整数排序算法，其原理是将整数按位数切割成不同的数字，然后按每个位数分别比较。由于整数也可以表达字符串（比如名字或日期）和特定格式的浮点数，所以基数排序也不是只能使用于整数。
基数排序 vs 计数排序 vs 桶排序
基数排序有两种方法：
这三种排序算法都利用了桶的概念，但对桶的使用方法上有明显差异：
基数排序：根据键值的每位数字来分配桶；
计数排序：每个桶只存储单一键值；
桶排序：每个桶存储一定范围的数值；
'''


def radix_sort(array):
    max_num = max(array)
    place = 1
    while max_num >= 10 ** place:
        place += 1
    for i in range(place):
        buckets = [[] for _ in range(10)]
        for num in array:
            radix = int(num / (10 ** i) % 10)
            buckets[radix].append(num)
        j = 0
        for k in range(10):
            for num in buckets[k]:
                array[j] = num
                j += 1
    return array

arr = [2,1,32,41,42,33,4545,0,343,434,34232,44,3434,43,543,48,5]
print(radix_sort(arr))
