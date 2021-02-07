def combination(combine: int, total: int) -> float:
    res = 1
    for k in range(0, combine):
        res = res * (total - k) / (combine - k)
    return res
