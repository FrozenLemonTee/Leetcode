"""
48. 旋转图像

给定一个 n × n 的二维矩阵表示一个图像。

将图像顺时针旋转 90 度。

说明：

你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

示例 1:

给定 matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

示例 2:

给定 matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

原地旋转输入矩阵，使其变为:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
"""
from typing import List


def rotate(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    bottom = len(matrix) - 1
    if bottom > 0:
        left = top = 0
        right = len(matrix[0]) - 1
        while left < right and top < bottom:
            tmp = matrix[top][left: right]
            for i in range(0, bottom - top):
                tmp[i], matrix[i+top][right] = matrix[i+top][right], tmp[i]
            for i in range(0, bottom - top):
                tmp[i], matrix[bottom][right-i] = matrix[bottom][right-i], tmp[i]
            for i in range(0, bottom - top):
                tmp[i], matrix[bottom-i][left] = matrix[bottom-i][left], tmp[i]
            matrix[top][left: right] = tmp
            left += 1
            right -= 1
            top += 1
            bottom -= 1


if __name__ == "__main__":
    test = [
        [1, 3, 5],
        [7, 9, 11],
        [13, 15, 17]
    ]
    rotate(test)
    print(test)
    test2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    rotate(test2)
    print(test2)
