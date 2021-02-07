"""
24. 两两交换链表中的节点

给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。



示例:

给定 1->2->3->4, 你应该返回 2->1->4->3.


"""
# Definition for singly-linked list.
from DSAA.data_structure.basic.LeetcodeNode import ListNode


def swapPairs(head: ListNode or None) -> ListNode:
    if not head:
        return head
    p = ListNode("NULL", head)
    node_pointer1 = p
    while node_pointer1.next.next:
        node_pointer2 = node_pointer1.next.next.next
        node_pointer3 = node_pointer1.next.next
        node_pointer3.next = node_pointer1.next
        node_pointer1.next.next = node_pointer2
        node_pointer1.next = node_pointer3
        if node_pointer2 and node_pointer2.next:
            node_pointer1 = node_pointer1.next.next
        else:
            break
    return p.next


if __name__ == "__main__":
    test = ListNode(2, ListNode(1, ListNode(5, ListNode(4))))
    print(swapPairs(test))
    test2 = ListNode(2, ListNode(1, ListNode(5)))
    print(swapPairs(test2))
    test3 = ListNode(2, ListNode(1))
    print(swapPairs(test3))
    print(swapPairs(ListNode(1)))
    print(swapPairs(None))
