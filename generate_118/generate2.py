"""
118. 杨辉三角

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

"""
from typing import List


def generate(num_rows: int) -> List[List[int]]:
    result = []
    for i in range(0, num_rows):
        cur = [1]
        if not result:
            result.append(cur)
            continue
        for j in range(0, len(result[-1]) - 1):
            cur.append(result[-1][j] + result[-1][j + 1])
        cur.append(1)
        result.append(cur)
    return result


if __name__ == "__main__":
    print(generate(10))
