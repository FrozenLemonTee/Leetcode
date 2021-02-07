"""
43. 字符串相乘

给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:

输入: num1 = "2", num2 = "3"
输出: "6"

示例 2:

输入: num1 = "123", num2 = "456"
输出: "56088"

说明：

    num1 和 num2 的长度小于110。
    num1 和 num2 只包含数字 0-9。
    num1 和 num2 均不以零开头，除非是数字 0 本身。
    不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。


"""
from typing import List


def multiply(num1: str, num2: str) -> str:
    def fullAdd(p_num1: int, p_num2: int, p_carry: int, result_list: List[int]) -> int:
        summary = (p_num1 + p_num2 + p_carry)
        result_list.append(summary % 10)
        if summary > 9:
            p_carry = 1
        else:
            p_carry = 0
        return p_carry

    def plus(p_list1: List[int], p_list2: List[int]) -> List[int]:
        if len(p_list1) < len(p_list2):
            p_list1, p_list2 = p_list2, p_list1
        for k in range(0, len(p_list1) - len(p_list2)):
            p_list2.append(0)
        list3 = []
        p_index = 0
        p_carry = fullAdd(p_list1[p_index], p_list2[p_index], 0, list3)
        while True:
            if p_index < len(p_list1) - 1:
                p_index += 1
            p_carry = fullAdd(p_list1[p_index], p_list2[p_index], p_carry, list3)
            if p_index >= len(p_list1) - 1 and p_index >= len(p_list2) - 1:
                if p_carry > 0:
                    list3.append(p_carry)
                break
        return list3

    def singleMultiply(m_list: List[int], m_num: int) -> List[int]:
        if m_num == 0:
            return [0]
        else:
            m_result = []
            m_index = 0
            tmp = m_list[m_index] * m_num
            m_result.append(tmp % 10)
            if tmp > 9:
                m_carry = tmp // 10
            else:
                m_carry = 0
            m_index += 1
            while True:
                if m_index > len(m_list) - 1:
                    if m_carry > 0:
                        m_result.append(m_carry)
                    break
                else:
                    tmp = m_list[m_index] * m_num + m_carry
                    m_result.append(tmp % 10)
                    if tmp > 9:
                        m_carry = tmp // 10
                    else:
                        m_carry = 0
                if m_index <= len(m_list) - 1:
                    m_index += 1
        return m_result

    list1 = []
    list2 = []
    for num in num1:
        list1.insert(0, int(num))
    for num in num2:
        list2.insert(0, int(num))
    if len(list2) > len(list1):
        list1, list2 = list2, list1
    index = 0
    result = singleMultiply(list1, list2[index])
    while index < len(list2) - 1:
        index += 1
        temp = singleMultiply(list1, list2[index])
        for i in range(0, index):
            temp.insert(0, 0)
        result = plus(result, temp)
    ans = ""
    for j in range(len(result) - 1, -1, -1):
        ans += str(result[j])
    ans = ans.lstrip("0")
    if not ans:
        return "0"
    else:
        return ans


if __name__ == "__main__":
    print(multiply("1000", "3"))  # 3000
    print(multiply("3", "1000"))  # 3000
    print(multiply("207", "39"))  # 8073
    print(multiply("207", "0"))  # 0
    print(multiply("123", "456"))  # 56088
    print(multiply("12", "87"))  # 1044
    print(multiply("123456789", "987654321"))  # 121932631112635269
    print(multiply("8325921313256244", "843915323432552512"))
