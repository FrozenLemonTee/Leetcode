"""
552. 学生出勤记录 II

给定一个正整数 n，返回长度为 n 的所有可被视为可奖励的出勤记录的数量。 答案可能非常大，你只需返回结果mod 109 + 7的值。

学生出勤记录是只包含以下三个字符的字符串：

    'A' : Absent，缺勤
    'L' : Late，迟到
    'P' : Present，到场

如果记录不包含多于一个'A'（缺勤）或超过两个连续的'L'（迟到），则该记录被视为可奖励的。

示例 1:

输入: n = 2
输出: 8
解释：
有8个长度为2的记录将被视为可奖励：
"PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
只有"AA"不会被视为可奖励，因为缺勤次数超过一次。

注意：n 的值不会超过100000。
"""
from typing import List


def checkRecord(n: int) -> int:
    def iteration(s: List) -> List:
        res = []
        for mem in s:
            if mem[1] == 0:
                cur = mem[0] + "A"
                res.append([cur, 1])  # mem[1]为 A总数
            if mem[0][-2:] != "LL":
                cur = mem[0] + "L"
                res.append([cur, mem[1]])
            cur = mem[0] + "P"
            res.append([cur, mem[1]])
        return res

    ori = [["A", 1], ["L", 0], ["P", 0]]
    for i in range(0, n - 1):
        ori = iteration(ori)
    return len(ori)


if __name__ == "__main__":
    print(checkRecord(500))
