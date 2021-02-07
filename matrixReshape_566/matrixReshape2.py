"""
566. 重塑矩阵

在MATLAB中，有一个非常有用的函数 reshape，它可以将一个矩阵重塑为另一个大小不同的新矩阵，但保留其原始数据。

给出一个由二维数组表示的矩阵，以及两个正整数r和c，分别表示想要的重构的矩阵的行数和列数。

重构后的矩阵需要将原始矩阵的所有元素以相同的行遍历顺序填充。

如果具有给定参数的reshape操作是可行且合理的，则输出新的重塑矩阵；否则，输出原始矩阵。

示例 1:

输入:
nums =
[[1,2],
 [3,4]]
r = 1, c = 4
输出:
[[1,2,3,4]]
解释:
行遍历nums的结果是 [1,2,3,4]。新的矩阵是 1 * 4 矩阵, 用之前的元素值一行一行填充新矩阵。

示例 2:

输入:
nums =
[[1,2],
 [3,4]]
r = 2, c = 4
输出:
[[1,2],
 [3,4]]
解释:
没有办法将 2 * 2 矩阵转化为 2 * 4 矩阵。 所以输出原矩阵。

注意：

    给定矩阵的宽和高范围在 [1, 100]。
    给定的 r 和 c 都是正数。
"""
from typing import List


def matrixReshape(nums: List[List[int]], r: int, c: int) -> List[List[int]]:
    if len(nums) * len(nums[0]) == r * c:
        cur = 0
        row = []
        res = []
        for i in range(0, len(nums)):
            for j in range(0, len(nums[0])):
                if cur < c:
                    row.append(nums[i][j])
                    cur += 1
                else:
                    res.append(row)
                    cur = 1
                    row = [nums[i][j]]
        res.append(row)
        return res
    else:
        return nums


if __name__ == "__main__":
    test = [
        [1, 2], [3, 4], [5, 6], [7, 8]
    ]
    print(matrixReshape(test, 2, 4))
    test2 = [
        [1, 2], [3, 4]
    ]
    print(matrixReshape(test2, 4, 1))
