"""
152. 乘积最大子数组
给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
"""
from typing import List


def maxProduct(nums: List[int]) -> int:
    dp = [[float("-inf"), float("inf")] for _ in range(0, len(nums))]
    maxi = float("-inf")
    for i in range(0, len(dp)):
        if i == 0:
            dp[i][0] = nums[0]
            dp[i][1] = nums[0]
            maxi = max(maxi, dp[i][0])
            continue
        dp[i][0] = max(dp[i - 1][0] * nums[i], dp[i - 1][1] * nums[i], nums[i])
        dp[i][1] = min(dp[i - 1][0] * nums[i], dp[i - 1][1] * nums[i], nums[i])
        maxi = max(maxi, dp[i][0])
    return maxi


if __name__ == "__main__":
    print(maxProduct([-5, 3, 2, -7, 6, -8, 9]))
    print(maxProduct([-2]))
    print(maxProduct([2, -1, 1, 1]))
