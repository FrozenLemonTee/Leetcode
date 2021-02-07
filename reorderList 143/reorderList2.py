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
    def midNode() -> ListNode:
        dummy1 = ListNode("NULL", head)
        fast = slow = dummy1
        if dummy1.next:
            while fast.next:
                for i in range(0, 2):
                    if fast.next:
                        fast = fast.next
                slow = slow.next
        return slow

    def reverse(node: ListNode) -> None:
        pre = None
        cur = node.next
        la = cur.next
        node.next = None
        while cur:
            cur.next = pre
            pre = cur
            cur = la
            if la:
                la = la.next
        node.next = pre

    dummy = ListNode("NULL", head)
    front = dummy
    if dummy.next and dummy.next.next:
        front = front.next
        last = midNode()
        reverse(last)
        last = last.next
        tmp = front
        while tmp.next != last:
            tmp = tmp.next
        while last and front != tmp:
            tmp.next = last.next
            last.next = front.next
            front.next = last
            front = last.next
            last = tmp.next


if __name__ == "__main__":
    test = turnIntoList([1, 2, 3, 4, 5, 6, 7, 8])
    reorderList(test)
    print(test)
