# 初始化全0列表 1
A = [0 for i in range(10)]
print(A)

# 初始化全0列表 1
def list_zero(num):
    return [0 for i in range(num)]

print(list_zero(10))


# 初始化全0 字符串
print('0'*0)

# 初始化全0 字典
s = 'dskds'
print({x: 0 for x in s})