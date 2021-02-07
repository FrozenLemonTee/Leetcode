from Leetcode.findErrorNums.findErrorNums4 import findErrorNums

if __name__ == "__main__":
    test = [3, 2, 3, 4, 6, 5]
    print(findErrorNums(test))  # [3,1]
    test2 = [2, 2, 1]
    print(findErrorNums(test2))  # [2,3]
    test3 = [1, 1]
    print(findErrorNums(test3))  # [1,2]
    test4 = [1, 2, 2, 4]
    print(findErrorNums(test4))  # [2,3]
    test5 = [2, 3, 2]
    print(findErrorNums(test5))  # [2,1]
