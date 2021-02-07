"""
121. 买卖股票的最佳时机

给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。

注意：你不能在买入股票前卖出股票。



示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。

示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。


"""
from typing import List


def maxProfit(prices: List[int]) -> int:
    if not prices:
        return 0
    the_max = 0
    low = float("inf")
    for price in prices:
        if price < low:
            low = price
            continue
        if price - low > the_max:
            the_max = price - low
    return the_max


if __name__ == "__main__":
    test = [7, 1, 5, 3, 6, 4]
    print(maxProfit(test))
    test2 = [7, 6, 4, 3, 1]
    print(maxProfit(test2))
    test3 = []
    print(maxProfit(test3))
    test4 = [2, 1]
    print(maxProfit(test4))
    test5 = [7, 8, 5, 4, 11, 3, 2, 6, 8, 14, 9, 17, 10]
    print(maxProfit(test5))
    test6 = [2, 7, 1, 4]
    print(maxProfit(test6))
