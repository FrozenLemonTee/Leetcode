"""
445. 两数相加 II

给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。



进阶：

如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。



示例：

输入：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 8 -> 0 -> 7


"""


from typing import List

# Definition for singly-linked list.
from DSAA.data_structure.basic.LeetcodeNode import ListNode


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    def pushInStack(node: ListNode) -> List[int]:
        p = node
        result = []
        while p:
            result.append(p.val)
            p = p.next
        return result
    list1 = pushInStack(l1)
    list2 = pushInStack(l2)
    l3 = ListNode("NULL")
    carry = 0
    while True:
        the_sum = 0
        if list1:
            the_sum += list1.pop()
        if list2:
            the_sum += list2.pop()
        the_sum += carry
        if the_sum > 9:
            carry = 1
        else:
            carry = 0
        if not l3.next:
            l3.next = ListNode(the_sum % 10)
        else:
            new_pointer = ListNode(the_sum % 10, l3.next)
            l3.next = new_pointer
        if not list1 and not list2 and carry == 0:
            break
    return l3.next


if __name__ == "__main__":
    t1 = ListNode(4, ListNode(3, ListNode(2, ListNode(1))))
    t2 = ListNode(8, ListNode(7, ListNode(2, ListNode(1))))
    print(t1)
    print(t2)
    print(addTwoNumbers(t1, t2))
