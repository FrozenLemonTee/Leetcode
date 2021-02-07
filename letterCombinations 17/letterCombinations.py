"""
17. 电话号码的字母组合

给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。

"""
from typing import List


def letterCombinations(digits: str) -> List[str]:
    mapping = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }
    length = len(digits)

    def buildChildStr(index_d: int) -> List[str]:
        child = []
        if index_d < length - 1:
            for char in mapping[digits[index_d]]:
                for res in buildChildStr(index_d + 1):
                    child.append("{0}{1}".format(char, res))
        else:
            return mapping[digits[index_d]]
        return child

    if digits:
        return buildChildStr(0)
    else:
        return []


if __name__ == "__main__":
    print(letterCombinations("2233"))
