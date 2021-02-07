"""
143. 重排链表

给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例 1:

给定链表 1->2->3->4, 重新排列为 1->4->2->3.

示例 2:

给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
"""

# Definition for singly-linked list.
from DSAA.data_structure.basic.LeetcodeNode import ListNode, turnIntoList


def reorderList(head: ListNode) -> None:
    # 正确，但是超时
    dummy = ListNode("NULL", head)
    last = front = dummy
    if dummy.next and dummy.next.next:
        while last.next:
            last = last.next
        tmp = front.next
        front = tmp
        while front != last and front.next != last:
            while tmp.next != last:
                tmp = tmp.next
            last.next = front.next
            tmp.next = None
            front.next = last
            last = tmp
            front = front.next
            tmp = front.next
            front = tmp


if __name__ == "__main__":
    test = turnIntoList([1, 2, 3, 4, 5])
    reorderList(test)
    print(test)
