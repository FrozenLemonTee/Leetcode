"""
53. 最大子序和

给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

"""
from typing import List


def maxSubArray(nums: List[int]) -> int:
    # 动态规划
    if not nums:
        return -2147483648
    result = -2147483648
    dp = 0
    for i in range(0, len(nums)):
        dp = max(dp + nums[i], nums[i])
        result = max(result, dp)
        # print("dp[{0}] = {1}, result[{2}] = {3}".format(i, dp, i, result))
    return max(result, dp)


if __name__ == "__main__":
    print(maxSubArray([-1]))
    print(maxSubArray([]))
    test2 = [-2, 1, -3, 4, -1, 2, 1, -5, 4, 8, 12, -10, 9, 11, 13, 12, 11, -7, -11, 15]
    print(maxSubArray(test2))  # 71
    test = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(maxSubArray(test))  # 6
