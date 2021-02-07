"""
13. 罗马数字转整数

罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为
IX。这个特殊的规则只适用于以下六种情况：

    I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
    X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。
    C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。

给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

示例 1:

输入: "III"
输出: 3

示例 2:

输入: "IV"
输出: 4

示例 3:

输入: "IX"
输出: 9

示例 4:

输入: "LVIII"
输出: 58
解释: L = 50, V= 5, III = 3.

示例 5:

输入: "MCMXCIV"
输出: 1994
解释: M = 1000, CM = 900, XC = 90, IV = 4.


"""


def romanToInt(s: str) -> int:
    """罗马数字转换 简化版"""
    tran = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "v": 5000, "x": 10000, "l": 50000,
            "c": 100000,
            "d": 500000, "m": 1000000}
    result = 0
    tmp = []
    i = 0
    for j in range(0, 2):
        if j > len(s) - 1:
            break
        tmp.append(s[j])
        j += 1
        i = j
    while len(tmp) > 0:
        if len(tmp) < 2 and i <= len(s) - 1:
            tmp.append(s[i])
            i += 1
            continue
        if len(tmp) == 1:
            result += tran[tmp.pop()]
        elif len(tmp) == 2:
            if tran[tmp[0]] >= tran[tmp[1]]:
                result += tran[tmp.pop(0)]
            else:
                result += (- tran[tmp.pop(0)])
        if i <= len(s) - 1:
            i += 1
            tmp.append(s[i-1])
    return result


if __name__ == "__main__":
    test = "XC"
    print(romanToInt(test))
