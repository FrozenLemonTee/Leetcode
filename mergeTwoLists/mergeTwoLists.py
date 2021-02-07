"""
21. 合并两个有序链表

将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。



示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4


"""


# Definition for singly-linked list.
from DSAA.data_structure.basic.LeetcodeNode import ListNode


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    node_pointer1 = l1
    node_pointer2 = l2
    l3 = node_pointer3 = ListNode("NULL")
    while node_pointer1 or node_pointer2:
        if not l2:
            l1 = l1.next
            node_pointer3.next = node_pointer1
            node_pointer1.next = None
            node_pointer1 = l1
            node_pointer3 = node_pointer3.next
            continue
        if not l1:
            l2 = l2.next
            node_pointer3.next = node_pointer2
            node_pointer2.next = None
            node_pointer2 = l2
            node_pointer3 = node_pointer3.next
            continue
        if type(node_pointer1.val) is str:
            l1 = l1.next
            node_pointer3.next = node_pointer1
            node_pointer1.next = None
            node_pointer1 = l1
            node_pointer3 = node_pointer3.next
            continue
        if type(node_pointer2.val) is str:
            l2 = l2.next
            node_pointer3.next = node_pointer2
            node_pointer2.next = None
            node_pointer2 = l2
            node_pointer3 = node_pointer3.next
            continue
        if node_pointer1.val < node_pointer2.val:
            l1 = l1.next
            node_pointer3.next = node_pointer1
            node_pointer1.next = None
            node_pointer1 = l1
        else:
            l2 = l2.next
            node_pointer3.next = node_pointer2
            node_pointer2.next = None
            node_pointer2 = l2
        node_pointer3 = node_pointer3.next
    return l3.next


if __name__ == "__main__":
    m2 = ListNode(3)
    m1 = ListNode(-9, m2)
    n2 = ListNode(7)
    n1 = ListNode(5, n2)
    print(n1)
    print(m1)
    print("result:")
    print(mergeTwoLists(m1, n1))
    t1 = ListNode("NULL")
    t2 = ListNode("NULL", ListNode(1, ListNode(3, ListNode(5, ListNode(7)))))
    print(mergeTwoLists(t1, t2))
