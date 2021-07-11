def sum(li):
    sum = 0
    li1 = []
    for i in range(len(li)):
        for j in range(i):
            if li[j] < li[i]:
                sum += li[j]
                li1.append(li[j])


    return (li1,sum)

li = [1,3,4,2,5]
print(sum(li))


def repat(s):
    occ = set()
    n = len(s)

    r1,r2=-1,0
    for i in range(n):
        if i!=0:
            occ.remove(s[i-1])

        while r1+1 <n and s[r1+1] not in occ:
            occ.add(s[r1+1])
            r1 += 1
        r2 = max(r2,r1-i+1)

    return r2

s = 'dsjjfnlsdfdfgk'
print(repat(s))

import math
print (int(math.sqrt(16)))
print (math.isqrt(16))


