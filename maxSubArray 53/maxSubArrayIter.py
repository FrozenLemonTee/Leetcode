from typing import List


class maxSubArray:
    def __init__(self, nums: List[int] or List[None]):
        self.nums = nums
        self.isBegin = 0
        self.index = 0
        self.dp = 0
        self.result = -2147483648
        if not self.isEmpty():
            self.dp = max(self.dp + self.nums[self.index], self.nums[self.index])
        self.result = max(self.result, self.dp)

    def isIterable(self):
        return self.index < len(self.nums) - 1

    def isIterationBegin(self):
        return self.isBegin

    def isEmpty(self):
        return not self.nums

    def __iter__(self):
        return self

    def __next__(self):
        if not self.isIterationBegin():
            self.isBegin = 1
            return self.result
        if self.isIterable():
            self.index += 1
            self.dp = max(self.dp + self.nums[self.index], self.nums[self.index])
            self.result = max(self.result, self.dp)
            return self.result
        else:
            raise StopIteration

    def __repr__(self):
        info = "Iteration_maxSubArray<#{}".format(id(self))
        if self.isIterationBegin():
            info += ", dp[{0}] = {1}, result[{2}] = {3}, isIterable() = {4}".format(self.index, self.dp, self.index, self.result, self.isIterable())
        return info + ">"


if __name__ == "__main__":
    test2 = [-2, 1, -3, 4, -1, 2, 1, -5, 4, 8, 12, -10, 9, 11, 13, 12, 11, -7, -11, 15]
    iteration1 = maxSubArray(test2)
    print()
    print(iteration1)
    print()
    for iteration in iteration1:
        print(iteration1)
        print(iteration)
    print()
    try:
        next(iteration1)
    except StopIteration:
        print("StopIteration")
    print(iteration1)
    print()
    iteration2 = maxSubArray([7])
    print(iteration2)
    print()
    for iteration in iteration2:
        print(iteration2)
        print(iteration)
    print()
    try:
        next(iteration2)
    except StopIteration:
        print("StopIteration")
        print(iteration2)
    else:
        print(iteration2)
