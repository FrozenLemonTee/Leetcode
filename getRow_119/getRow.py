"""
119. 杨辉三角 II

给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。

在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 3
输出: [1,3,3,1]

进阶：

你可以优化你的算法到 O(k) 空间复杂度吗
"""
from typing import List


def getRow(row_index: int) -> List[int]:
    def combination(combine: int, total: int) -> float:
        res = 1
        for k in range(0, combine):
            res = res * (total - k) / (combine - k)
        return res
    row_index += 1
    result = []
    for i in range(0, row_index):
        result.append(round(combination(i, row_index - 1)))
    return result


if __name__ == "__main__":
    for j in range(0, 34):
        print(getRow(j))
