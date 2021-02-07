"""
506. 相对名次

给出 N 名运动员的成绩，找出他们的相对名次并授予前三名对应的奖牌。前三名运动员将会被分别授予 “金牌”，“银牌” 和“ 铜牌”（"Gold Medal", "Silver Medal", "Bronze Medal"）。

(注：分数越高的选手，排名越靠前。)

示例 1:

输入: [5, 4, 3, 2, 1]
输出: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
解释: 前三名运动员的成绩为前三高的，因此将会分别被授予 “金牌”，“银牌”和“铜牌” ("Gold Medal", "Silver Medal" and "Bronze Medal").
余下的两名运动员，我们只需要通过他们的成绩计算将其相对名次即可。

提示:

    N 是一个正整数并且不会超过 10000。
    所有运动员的成绩都不相同。
"""
from typing import List


def findRelativeRanks(nums: List[int]) -> List[str]:
    sort = []
    template = {1: "Gold Medal", 2: "Silver Medal", 3: "Bronze Medal"}
    for i in range(0, len(nums)):
        sort.append((nums[i], i))
    sort = sorted(sort, key=lambda item: item[0], reverse=True)
    for j in range(0, len(sort)):
        if j + 1 in template.keys():
            sort[j] = (template[j + 1], sort[j][1])
        else:
            sort[j] = (str(j + 1), sort[j][1])
    sort = sorted(sort, key=lambda item: item[1])
    return [item[0] for item in sort]


if __name__ == "__main__":
    print(findRelativeRanks([1, 4, 3, 2, 5, 6, 8, 7]))
