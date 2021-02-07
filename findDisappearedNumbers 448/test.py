from Leetcode.findDisappearedNumbers.findDisappearedNumbers3 import findDisappearedNumbers

if __name__ == "__main__":
    test = [3, 4, 4, 6, 7, 2, 2]  # [1, 5]
    print(findDisappearedNumbers(test))
    test2 = [4, 3, 2, 7, 8, 2, 3, 1]
    print(findDisappearedNumbers(test2))  # [5,6]
    test3 = [1, 1]
    print(findDisappearedNumbers(test3))  # [1]
    test4 = [10, 2, 5, 10, 9, 1, 1, 4, 3, 7]
    print(findDisappearedNumbers(test4))