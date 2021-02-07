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
    dic_sort = {}
    template = {1: "Gold Medal", 2: "Silver Medal", 3: "Bronze Medal"}
    for i in range(0, len(nums)):
        dic_sort.update({nums[i]: i})
    dic_sort = sorted(dic_sort.items(), key=lambda d: d[0], reverse=True)
    dic = {}
    order = 1
    for item in dic_sort:
        if order in template.keys():
            dic.update({template[order]: item[1]})
        else:
            dic.update({str(order): item[1]})
        order += 1
    ans = sorted(dic.items(), key=lambda c: c[1])
    return [o[0] for o in ans]


if __name__ == "__main__":
    print(findRelativeRanks([1, 4, 3, 2, 5, 6, 8, 7]))
