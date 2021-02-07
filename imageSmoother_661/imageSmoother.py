"""
661. 图片平滑器

包含整数的二维矩阵 M 表示一个图片的灰度。你需要设计一个平滑器来让每一个单元的灰度成为平均灰度 (向下舍入) ，平均灰度的计算是周围的8个单元和它本身的值求平均，如果周围的单元格不足八个，则尽可能多的利用它们。

示例 1:

输入:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
输出:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
解释:
对于点 (0,0), (0,2), (2,0), (2,2): 平均(3/4) = 平均(0.75) = 0
对于点 (0,1), (1,0), (1,2), (2,1): 平均(5/6) = 平均(0.83333333) = 0
对于点 (1,1): 平均(8/9) = 平均(0.88888889) = 0

注意:

    给定矩阵中的整数范围为 [0, 255]。
    矩阵的长和宽的范围均为 [1, 150]。
"""
from typing import List


def imageSmoother(m: List[List[int]]) -> List[List[int]]:
    size_x = len(m)
    size_y = 0
    if size_x > 0:
        size_y = len(m[0])
    result = []
    for i in range(0, size_x):
        line = []
        for j in range(0, size_y):
            average = []
            for p in range(i - 1, i + 2):
                if p < 0 or p >= size_x:
                    continue
                for q in range(j - 1, j + 2):
                    if q < 0 or q >= size_y:
                        continue
                    average.append(m[p][q])
            line.append(int(sum(average) / len(average)))
        result.append(line)
    return result


if __name__ == "__main__":
    test = [[4, 6, 0],
            [1, 5, 3],
            [2, 1, 7],
            [7, 4, 9]]
    print(imageSmoother(test))
