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


# Definition for singly-linked list.
from DSAA.data_structure.basic.LeetcodeNode import ListNode


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    def listSum(node: ListNode) -> int:
        p = node
        tmp = []
        result = 0
        while p:
            tmp.append(p.val)
            p = p.next
        for i in range(1, len(tmp)+1):
            result += tmp[-i] * 10 ** (i-1)
        return result
    the_sum = listSum(l1) + listSum(l2)
    length = len(str(the_sum))
    node_pointer = l3 = ListNode("NULL")
    for j in range(length, 0, -1):
        node_pointer.next = ListNode(the_sum // (10 ** (j-1)))
        the_sum -= node_pointer.next.val * 10 ** (j - 1)
        node_pointer = node_pointer.next
    return l3.next


if __name__ == "__main__":
    q1 = ListNode(1, ListNode(2, ListNode(3)))
    q2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    print(addTwoNumbers(q1, q2))
