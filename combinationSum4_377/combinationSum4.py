"""
377. 组合总和 Ⅳ

给定一个由正整数组成且不存在重复数字的数组，找出和为给定目标正整数的组合的个数。

示例:

nums = [1, 2, 3]
target = 4

所有可能的组合为：
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

请注意，顺序不同的序列被视作不同的组合。

因此输出为 7。

进阶：
如果给定的数组中含有负数会怎么样？
问题会产生什么变化？
我们需要在题目中添加什么限制来允许负数的出现？

致谢：
特别感谢 @pbrother 添加此问题并创建所有测试用例。
"""
from typing import List


def combinationSum4(nums: List[int], target: int) -> int:
    # 超时
    res = [0]

    def trackBacking(summary: int) -> None:
        for num in nums:
            if summary + num < target:
                trackBacking(summary + num)
            elif summary + num == target:
                res[0] += 1
    trackBacking(0)
    return res[0]


if __name__ == "__main__":
    print(combinationSum4(sorted([4, 2, 1]), 19))
