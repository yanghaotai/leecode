'''
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。

输入：strs = ["flower","flow","flight"]
输出："fl"

输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。

'''

strs = ["flower","flow","flight"]
ss = sorted(strs,key=len)
print(ss)
ss1 = []
ss2 = []
for i in range(len(ss[0])):
    if ss[0][i] == ss[1][i]:
        ss1.append(ss[0][i])
    else:
        break

for j in range(len(ss1)):
    if ss1[j] == ss[2][j]:
        ss2.append(ss1[j])
    else:
        break
print(''.join(ss2))

