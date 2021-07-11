'''
118. 杨辉三角
难度 简单

给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:
输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

'''


def generate(numRows: int) -> list[list[int]]:
    ret = []
    for i in range(1, numRows + 1):
        tmp = [1 for _ in range(i)]
        for j in range(1, len(tmp) - 1):
            # 这里注意是 i - 2
            tmp[j] = ret[i - 2][j - 1] + ret[i - 2][j]
        ret.append(tmp)
    return ret


print(generate(5))