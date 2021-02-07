"""
128. 最长连续序列

给定一个未排序的整数数组，找出最长连续序列的长度。

要求算法的时间复杂度为 O(n)。

示例:

输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。


"""
from typing import List


def longestConsecutive(nums: List[int]) -> int:
    # 超时
    if not nums:
        return 0
    dic = set(nums)
    the_max = tmp = 0
    for i in range(min(dic), max(dic) + 1):
        if i in dic:
            tmp += 1
        else:
            the_max = max(the_max, tmp)
            tmp = 0
    return max(the_max, tmp)


if __name__ == "__main__":
    test1 = [0]
    print(longestConsecutive(test1))
    test2 = [100, 4, 200, 1, 3, 2]
    print(longestConsecutive(test2))
    test3 = []
    print(longestConsecutive(test3))
