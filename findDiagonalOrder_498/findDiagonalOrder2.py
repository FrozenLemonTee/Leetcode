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
        up = 1
        cur_i = cur_j = 0
        while True:
            line = []
            i = cur_i
            j = cur_j
            while i + j == cur_i + cur_j:
                line.append(matrix[j][i])
                if j - 1 >= 0 and i + 1 <= size_x:
                    j -= 1
                    i += 1
                else:
                    break
            if up == 0:
                for k in range(0, (len(line) - 1) // 2 + 1):
                    line[k], line[-(k+1)] = line[-(k+1)], line[k]
                up = 1
            else:
                up = 0
            res += line
            if cur_j + 1 <= size_y:
                cur_j += 1
            elif cur_i + 1 <= size_x:
                cur_i += 1
            else:
                return res
    return []


if __name__ == "__main__":
    test = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
    ]
    print(findDiagonalOrder(test))
