"""
575. 分糖果

给定一个偶数长度的数组，其中不同的数字代表着不同种类的糖果，每一个数字代表一个糖果。你需要把这些糖果平均分给一个弟弟和一个妹妹。返回妹妹可以获得的最大糖果的种类数。

示例 1:

输入: candies = [1,1,2,2,3,3]
输出: 3
解析: 一共有三种种类的糖果，每一种都有两个。
     最优分配方案：妹妹获得[1,2,3],弟弟也获得[1,2,3]。这样使妹妹获得糖果的种类数最多。

示例 2 :

输入: candies = [1,1,2,3]
输出: 2
解析: 妹妹获得糖果[2,3],弟弟获得糖果[1,1]，妹妹有两种不同的糖果，弟弟只有一种。这样使得妹妹可以获得的糖果种类数最多。

注意:

    数组的长度为[2, 10,000]，并且确定为偶数。
    数组中数字的大小在范围[-100,000, 100,000]内。
"""
from typing import List


def distributeCandies(candies: List[int]) -> int:
    candie_list = {}
    length = len(candies)
    for candie in candies:
        if candie not in candie_list.keys():
            candie_list.update({candie: 1})
        else:
            candie_list[candie] += 1
    count = 0
    result = 0
    for candie in sorted(candie_list.items(), key=lambda item: item[1]):
        if count < length / 2:
            count += 1
            result += 1
        else:
            break
    return result


if __name__ == "__main__":
    test = [1, 1, 2, 3]
    print(distributeCandies(test))  # 2
    test2 = [1, 1, 2, 2, 3, 3]
    print(distributeCandies(test2))  # 3
