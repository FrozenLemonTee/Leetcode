"""
412. Fizz Buzz

写一个程序，输出从 1 到 n 数字的字符串表示。

1. 如果 n 是3的倍数，输出“Fizz”；

2. 如果 n 是5的倍数，输出“Buzz”；

3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。

示例：

n = 15,

返回:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
"""
from typing import List


def fizzBuzz(n: int) -> List[str]:
    res = []
    for i in range(1, n + 1):
        cur = ""
        if i % 3 == 0:
            cur += "Fizz"
        if i % 5 == 0:
            cur += "Buzz"
        if i % 3 != 0 and i % 5 != 0:
            cur += str(i)
        res.append(cur)
    return res
