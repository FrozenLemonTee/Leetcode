"""
两数之和

给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。



示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    """暴力解法（未通过：超出时间限制）"""
    # if len(nums) == 0 or len(nums) == 1:
    #     return []
    # i = 0
    # while True:
    #     j = i + 1
    #     while True:
    #         if nums[i] + nums[j] == target:
    #             return [i, j]
    #         if j == len(nums) - 1:
    #             break
    #         j = j + 1
    #     if i == len(nums) - 2 and j == len(nums) - 1:
    #         break
    #     i = i + 1
    # return []

    """利用二分查找法"""
    tmp = nums.copy()
    tmp.sort()
    if len(tmp) == 0 or len(tmp) == 1:
        return []
    last_index = len(tmp) - 1
    for i in range(0, last_index):
        solution = target - tmp[i]
        start = i + 1
        end = last_index
        while start <= end:
            mid = (start + end) // 2
            if solution < tmp[mid]:
                end = mid - 1
            elif solution > tmp[mid]:
                start = mid + 1
            else:
                index1 = nums.index(tmp[i])
                index2 = nums.index(tmp[mid])
                if index1 == index2:
                    index2 = nums[index1 + 1:].index(tmp[mid]) + (index1 + 1)
                if index1 > index2:
                    index1, index2 = index2, index1
                return [index1, index2]
    return []


if __name__ == "__main__":
    test = [-1, -2, -3, -4, -5]
    print(twoSum(test, -8))
