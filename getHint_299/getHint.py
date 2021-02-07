"""
299. 猜数字游戏

你在和朋友一起玩 猜数字（Bulls and Cows）游戏，该游戏规则如下：

    你写出一个秘密数字，并请朋友猜这个数字是多少。
    朋友每猜测一次，你就会给他一个提示，告诉他的猜测数字中有多少位属于数字和确切位置都猜对了（称为“Bulls”, 公牛），有多少位属于数字猜对了但是位置不对（称为“Cows”, 奶牛）。
    朋友根据提示继续猜，直到猜出秘密数字。

请写出一个根据秘密数字和朋友的猜测数返回提示的函数，返回字符串的格式为 xAyB ，x 和 y 都是数字，A 表示公牛，用 B 表示奶牛。

    xA 表示有 x 位数字出现在秘密数字中，且位置都与秘密数字一致。
    yB 表示有 y 位数字出现在秘密数字中，但位置与秘密数字不一致。

请注意秘密数字和朋友的猜测数都可能含有重复数字，每位数字只能统计一次。



示例 1:

输入: secret = "1807", guess = "7810"
输出: "1A3B"
解释: 1 公牛和 3 奶牛。公牛是 8，奶牛是 0, 1 和 7。

示例 2:

输入: secret = "1123", guess = "0111"
输出: "1A1B"
解释: 朋友猜测数中的第一个 1 是公牛，第二个或第三个 1 可被视为奶牛。



说明: 你可以假设秘密数字和朋友的猜测数都只包含数字，并且它们的长度永远相等。
"""


def getHint(secret: str, guess: str) -> str:
    digit = {}
    for i in range(0, len(secret)):
        if secret[i] not in digit.keys():
            digit.update({secret[i]: {i}})
        else:
            digit[secret[i]].update({i})
    x = y = 0
    visited = set()
    for j in range(0, len(guess)):
        if guess[j] in digit.keys():
            if j in digit[guess[j]]:
                visited.update({j})
                if len(digit[guess[j]]) == 1:
                    digit.pop(guess[j])
                else:
                    digit[guess[j]].remove(j)
                x += 1
    count = {}
    for j in range(0, len(guess)):
        if j in visited:
            continue
        else:
            if guess[j] in digit.keys():
                if guess[j] not in count.keys():
                    count.update({guess[j]: 1})
                    y += 1
                else:
                    count[guess[j]] += 1
                    if count[guess[j]] <= len(digit[guess[j]]):
                        y += 1
    return "{0}A{1}B".format(x, y)


if __name__ == "__main__":
    # print(getHint("11123", "04132"))
    print(getHint("1568467", "1230031"))
    print(getHint("168671536316", "123313261621"))
