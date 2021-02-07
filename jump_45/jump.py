"""
45. 跳跃游戏 II
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

示例:

输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
说明:

假设你总是可以到达数组的最后一个位置。
"""
from typing import List


def jump(nums: List[int]) -> int:
    # 正确但超时
    dp = [float("inf")] * len(nums)
    for i in range(0, len(dp)):
        if i == 0:
            dp[i] = 0
            continue
        if i == 1:
            dp[i] = 1
            continue
        cur = float("inf")
        for j in range(0, i):
            if nums[j] + j >= i:
                cur = min(cur, dp[j])
        dp[i] = cur + 1
    return int(dp[-1])


if __name__ == "__main__":
    print(jump([2, 3, 1, 1, 4]))
