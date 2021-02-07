"""
92. 反转链表 II

反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:

输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL
"""

# Definition for singly-linked list.
from DSAA.data_structure.basic.LeetcodeNode import ListNode, turnIntoList


def reverseBetween(head: ListNode, m: int, n: int) -> ListNode:
    dummy = ListNode("NULL", head)
    tmp_f = dummy
    for i in range(0, m - 1):
        tmp_f = tmp_f.next
    tmp_l = tmp_f
    for i in range(0, n - m + 2):
        tmp_l = tmp_l.next
    pre = None
    n_last = cur = tmp_f.next
    last = cur.next
    for i in range(0, n - m + 1):
        cur.next = pre
        pre = cur
        cur = last
        if last:
            last = last.next
    n_last.next = tmp_l
    tmp_f.next = pre
    return dummy.next


if __name__ == "__main__":
    test = turnIntoList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(reverseBetween(test, 3, 7))
