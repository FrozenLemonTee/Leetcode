"""
203. 移除链表元素

删除链表中等于给定值 val 的所有节点。

示例:

输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5


"""


# Definition for singly-linked list.
from DSAA.data_structure.basic.LeetcodeNode import ListNode


def removeElements(head: ListNode, val: int) -> ListNode:
    node_pointer = list_node = ListNode("NULL", ListNode("NULL", head))
    while node_pointer.next:
        if not node_pointer.next.next:
            if node_pointer.next.val == val:
                node_pointer.next = None
            break
        if node_pointer.next.val == val:
            node_pointer.next = node_pointer.next.next
            continue
        if node_pointer.next:
            node_pointer = node_pointer.next
    return list_node.next.next


if __name__ == "__main__":
    l1 = ListNode(1, ListNode(2, ListNode(6, ListNode(5, ListNode(9, ListNode(6))))))
    print(l1)
    print(removeElements(l1, 6))
    l2 = ListNode(1, ListNode(1))
    print(l2)
    print(removeElements(l2, 1))
