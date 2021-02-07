"""
442. 数组中重复的数据

给定一个整数数组 a，其中1 ≤ a[i] ≤ n （n为数组长度）, 其中有些元素出现两次而其他元素出现一次。

找到所有出现两次的元素。

你可以不用到任何额外空间并在O(n)时间复杂度内解决这个问题吗？

示例：

输入:
[4,3,2,7,8,2,3,1]

输出:
[2,3]


"""
from typing import List


def findDuplicates(nums: List[int]) -> List[int]:
    # 哈希表：原地哈希
    result = []
    for i in range(0, len(nums)):
        if nums[abs(nums[i]) - 1] > 0:
            nums[abs(nums[i]) - 1] *= -1
        else:
            result.append(abs(nums[i]))
    return result


if __name__ == "__main__":
    test = [4, 3, 2, 7, 8, 2, 3, 1]
    print(findDuplicates(test))
