"""
498. 对角线遍历

给定一个含有 M x N 个元素的矩阵（M 行，N 列），请以对角线遍历的顺序返回这个矩阵中的所有元素，对角线遍历如下图所示。



示例:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

输出:  [1,2,4,7,5,3,6,8,9]

说明:
    给定矩阵中的元素总数不会超过 100000 。
"""
from typing import List


def findDiagonalOrder(matrix: List[List[int]]) -> List[int]:
    if matrix:
        res = []
        size_y = len(matrix) - 1
        size_x = len(matrix[0]) - 1
        i = j = 0
        up = 1
        while True:
            if up == 1:
                up = 0
                while True:
                    res.append(matrix[j][i])
                    if i == size_x and j == size_y:
                        return res
                    if j > 0 and i < size_x:
                        j -= 1
                        i += 1
                    else:
                        if i < size_x:
                            i += 1
                        elif j < size_y:
                            j += 1
                        break
            else:
                up = 1
                while True:
                    res.append(matrix[j][i])
                    if i == size_x and j == size_y:
                        return res
                    if j < size_y and i > 0:
                        j += 1
                        i -= 1
                    else:
                        if j < size_y:
                            j += 1
                        elif i < size_x:
                            i += 1
                        break
    return []


if __name__ == "__main__":
    test = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
    ]
    print(findDiagonalOrder(test))
