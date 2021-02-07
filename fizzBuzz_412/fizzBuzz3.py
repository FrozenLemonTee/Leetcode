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
from collections import OrderedDict


def fizzBuzz(n: int) -> List[str]:
    diff = OrderedDict({3: "Fizz", 5: "Buzz"})
    res = []
    for i in range(1, n + 1):
        flag = 0
        cur = ""
        for num in diff.keys():
            if i % num == 0:
                cur += diff[num]
                flag = 1
        if flag == 0:
            cur += str(i)
        res.append(cur)
    return res


if __name__ == "__main__":
    print(fizzBuzz(15))
