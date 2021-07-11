version1 = "7.5.2.4"
version2 = "7.5.3"

s1 = version1.split('.')
s2 = version2.split('.')
print(s1,s2)

def com(s1,s2):
    len1 = min(len(s1),len(s2))
    for i in range(len1):
        if int(s1[i])>int(s2[i]):
            return 1
        elif int(s1[i])<int(s2[i]):
            return -1
        else:
            continue

    if len(s1)==len(s2):
        return 0
    elif len(s1)>len(s2):
        for j in range(len1,len(s1)):
            if int(s1[j])!=0:
                return 1
        else:
            return 0
    else:
        for j in range(len1,len(s2)):
            if int(s2[j])!=0:
                return -1
        else:
            return 0

print(com(s1,s2))

