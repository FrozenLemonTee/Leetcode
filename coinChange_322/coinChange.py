"""
322. 零钱兑换
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

你可以认为每种硬币的数量是无限的。



示例 1：

输入：coins = [1, 2, 5], amount = 11
输出：3
解释：11 = 5 + 5 + 1
示例 2：

输入：coins = [2], amount = 3
输出：-1
示例 3：

输入：coins = [1], amount = 0
输出：0
示例 4：

输入：coins = [1], amount = 1
输出：1
示例 5：

输入：coins = [1], amount = 2
输出：2


提示：

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
"""
from typing import List


def coinChange(coins: List[int], amount: int) -> int:
    """思路：动态规划"""
    """1.确定状态"""
    #  状态用函数表示： m为金额数，dp[m]为此（金额）状态下最少可以凑到的硬币数
    #  本题m为自然数，则m = amount 给定时所有要求的金额状态有m = 0, 1, 2, ..., amount - 1, amount (总共有 amount + 1种情况，数组长为 amount + 1)
    """2.转移方程"""
    #  dp[m] = min(dp[m - coins[0]], dp[m - coins[1]], dp[m - coins[2]], ..., dp[m - coins[len(coins) - 2]], dp[m - coins[len(coins) - 1]]) + 1
    """3.边界条件与初始情况"""
    #  这两类特例是为了控制转移方程的活动范围
    #  (1) 只要找不到用多少枚硬币能拼凑的情况，都有dp[k] = float("inf")
    #  (2) 当 m = 0 时，显然有 dp[0] = 0.
    """4.确定求解顺序"""
    #  从m = 0 依次递增
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    for i in range(1, len(dp)):
        cur = float("inf")
        for j in range(0, len(coins)):
            if i - coins[j] >= 0:
                cur = min(cur, dp[i - coins[j]])
        dp[i] = cur + 1
    if dp[amount] == float("inf"):
        return -1
    return int(dp[amount])


if __name__ == "__main__":
    print(coinChange([1, 2, 5], 11))
    print(coinChange([1, 2, 5, 10, 20, 50, 100], 85))
