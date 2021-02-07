"""
54. 螺旋矩阵

给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例 1:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]

示例 2:

输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]
"""
from typing import List


def spiralOrder(matrix: List[List[int]]) -> List[int]:
    res = []
    while matrix:
        while matrix[0]:
            res.append(matrix[0].pop(0))
        matrix.pop(0)
        if not matrix:
            break
        length = len(matrix)
        i = 0
        while i < length:
            res.append(matrix[i].pop(-1))
            if not matrix[i]:
                matrix.pop(0)
                length -= 1
                i -= 1
            i += 1
        if not matrix:
            break
        while matrix[-1]:
            res.append(matrix[-1].pop(-1))
        matrix.pop(-1)
        length = len(matrix)
        j = 0
        while j < length:
            res.append(matrix[(length - 1) - j].pop(0))
            if not matrix[(length - 1) - j]:
                matrix.pop((length - 1) - j)
                length -= 1
                j -= 1
            j += 1
    return res


if __name__ == "__main__":
    test = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    print(spiralOrder(test))
    test2 = [
        [7],
        [9],
        [6],
    ]
    print(spiralOrder(test2))
    test3 = [
        [1, 2],
        [3, 4],
        [5, 6],
        [7, 8],
    ]
    print(spiralOrder(test3))
    test4 = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25],
    ]
    print(spiralOrder(test4))
