"""
665. 非递减数列

给你一个长度为 n 的整数数组，请你判断在 最多 改变 1 个元素的情况下，该数组能否变成一个非递减数列。

我们是这样定义一个非递减数列的： 对于数组中所有的 i (0 <= i <= n-2)，总满足 nums[i] <= nums[i + 1]。



示例 1:

输入: nums = [4,2,3]
输出: true
解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。

示例 2:

输入: nums = [4,2,1]
输出: false
解释: 你不能在只改变一个元素的情况下将其变为非递减数列。



说明：

    1 <= n <= 10 ^ 4
    - 10 ^ 5 <= nums[i] <= 10 ^ 5
"""
from typing import List


def checkPossibility(nums: List[int]) -> bool:
    flag = 0
    nums.insert(0, - (10 ** 5 + 1))
    nums.append(10 ** 5 + 1)
    for i in range(1, len(nums) - 1):
        while not (nums[i - 1] <= nums[i] <= nums[i + 1]):
            if flag == 0:
                if nums[i - 1] > nums[i + 1]:
                    nums[i + 1] = max(nums[i], nums[i - 1])
                else:
                    nums[i] = min(nums[i - 1], nums[i + 1])
                flag = 1
            else:
                return False
    return True


if __name__ == "__main__":
    print(checkPossibility([3, 5, 7, 4, 8, 9]))  # True
    print(checkPossibility([4, 2, 3]))  # True
    print(checkPossibility([5, 7, 1, 8]))  # True
    print(checkPossibility([-1, 4, 2, 3]))  # True
    print(checkPossibility([3, 4, 2, 3]))  # False
    print(checkPossibility([4, 2, 1, 3, 5, 7, 9, 10]))  # False
