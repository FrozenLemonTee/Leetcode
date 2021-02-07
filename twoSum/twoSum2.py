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
    """排序+双指针"""
    tmp = nums.copy()
    tmp.sort()
    first_index = 0
    last_index = len(tmp) - 1
    while first_index <= last_index:
        solution = tmp[first_index] + tmp[last_index]
        if solution < target:
            first_index = first_index + 1
        elif solution > target:
            last_index = last_index - 1
        else:
            index1 = nums.index(tmp[first_index])
            index2 = nums.index(tmp[last_index])
            if index1 > index2:
                index1, index2 = index2, index1
            if index1 == index2:
                try:
                    index2 = nums[index1 + 1:].index(tmp[first_index]) + (index1 + 1)
                except ValueError:
                    return []
            return [index1, index2]
    return []


if __name__ == "__main__":
    test = [2, 7, 11, 15]
    print(twoSum(test, 9))
