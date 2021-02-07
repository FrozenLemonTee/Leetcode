"""
62. 不同路径
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？

示例 1:

输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右

示例 2:

输入: m = 7, n = 3
输出: 28


提示：

1 <= m, n <= 100
题目数据保证答案小于等于 2 * 10 ^ 9
"""


def uniquePaths(m: int, n: int) -> int:
    dp = [([0] * m) for _ in range(0, n)]
    for i in range(0, len(dp)):
        for j in range(0, len(dp[0])):
            if i == 0 and j == 0:
                dp[i][j] = 1
                continue
            if i == 0:
                dp[i][j] = dp[i][j - 1]
                continue
            if j == 0:
                dp[i][j] = dp[i - 1][j]
                continue
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[n - 1][m - 1]


if __name__ == "__main__":
    print(uniquePaths(5, 5))
    print(uniquePaths(3, 7))
