"""
91. 解码方法

一条包含字母 A-Z 的消息通过以下方式进行了编码：

'A' -> 1
'B' -> 2
...
'Z' -> 26

给定一个只包含数字的非空字符串，请计算解码方法的总数。

题目数据保证答案肯定是一个 32 位的整数。



示例 1：

输入：s = "12"
输出：2
解释：它可以解码为 "AB"（1 2）或者 "L"（12）。

示例 2：

输入：s = "226"
输出：3
解释：它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。

示例 3：

输入：s = "0"
输出：0

示例 4：

输入：s = "1"
输出：1

示例 5：

输入：s = "2"
输出：1



提示：

    1 <= s.length <= 100
    s 只包含数字，并且可能包含前导零
"""
from typing import List


def numDecodings(s: str) -> int:
    def theWays(s1: str) -> List[int]:
        # 判断字符串（len = 1, 2）可以被划分的子字符串的长度情况
        if len(s1) == 2:
            if int(s1) % 10 == 0:
                if 0 < int(s1[0]) < 3:
                    return [2]
                return []
            if int(s1) < 10 or int(s1) > 26:
                return [1]
            return [1, 2]
        return [1] if int(s1) != 0 else []

    dp = [0] * (len(s) + 1)
    for i in range(0, len(dp)):
        if i == 0:
            dp[0] = 1
            continue
        for way in theWays(s[i - 2 if i - 2 >= 0 else 0:  i]):
            if way == 1:
                dp[i] += dp[i - 1]
            if way == 2:
                dp[i] += dp[i - 2]
    return dp[-1]


if __name__ == "__main__":
    print(numDecodings("226"))
    print(numDecodings("12321"))
    print(numDecodings("01111"))
    print(numDecodings("01"))
    print(numDecodings("10"))
    print(numDecodings("2101"))
