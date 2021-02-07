"""
61. 旋转链表

给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL

示例 2:

输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL


"""

# Definition for singly-linked list.
from DSAA.data_structure.basic.LeetcodeNode import ListNode


def rotateRight(head: ListNode, k: int) -> ListNode:
    p = ListNode("NULL", head)
    if not p.next or not p.next.next:
        return p.next
    if not p.next.next.next:
        k = k % 2
        if k == 0:
            return p.next
        else:
            p.next.next.next = p.next
            p.next = p.next.next
            p.next.next.next = None
            return p.next
    node_pointer1 = p.next
    length = 1
    while node_pointer1.next:
        length += 1
        node_pointer1 = node_pointer1.next
    k = k % length
    if k == 0:
        return p.next
    else:
        node_pointer2 = p.next
        for i in range(length - 1, k, -1):
            node_pointer2 = node_pointer2.next
        node_pointer1.next = p.next
        p.next = node_pointer2.next
        node_pointer2.next = None
        return p.next


if __name__ == "__main__":
    t = ListNode(2, ListNode(5, ListNode(8, ListNode(4))))
    print(t)
    print(rotateRight(t, 2))  # 8->4->2->5
