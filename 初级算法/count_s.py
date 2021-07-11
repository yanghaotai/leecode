def count_str(s):
    lis = {}
    for i in s:
        lis[i]=s.count(i)
    return lis

s = 'jdsjddsnmdsmdds'
print(count_str(s))


def count_str1(s):
    set1 = set(list(s))
    lis = {}
    for i in set1:
        lis[i] = 0
        for j in s:
            if j==i:
                lis[i] += 1
    return lis

s1 = 'dsdndfngfesfd'
print(count_str(s1))
print(count_str1(s1))

def count_str2(s):
    set1 = set(list(s))
    lis = {x:0 for x in s}
    for i in set1:
        for j in s:
            if j==i:
                lis[i] += 1
    return lis

s1 = 'dsdndfngfesfd'
print(count_str(s1))
print(count_str1(s1))
print(count_str2(s1))

s2 = 'sswweeww1'
print({i:s2.count(i) for i in s2})