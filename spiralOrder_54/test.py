from typing import List


def spiralOrder(matrix: List[List[int]]) -> List[int]:
    res = []
    while matrix:
        res += matrix.pop(0)
        matrix = list(zip(*matrix))[::-1]
    return res


if __name__ == "__main__":
    m1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    print(spiralOrder(m1))
