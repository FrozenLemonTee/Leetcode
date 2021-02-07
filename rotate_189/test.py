from Leetcode.rotate_189.rotate06 import rotate

if __name__ == "__main__":
    test = [-1, -100, 3, 99]
    rotate(test, -1)
    print(test)  # [-100, 3, 99, -1]
    test2 = [1]
    rotate(test2, 5)
    print(test2)  # [1]
    test3 = [1, 2, 3, 4, 5, 6, 7]
    rotate(test3, 9)
    print(test3)  # [6, 7, 1, 2, 3, 4, 5]
    test4 = [5, 8, 6, 10]
    rotate(test4, -7)
    print(test4)  # [10, 5, 8, 6]
