"""
19. 删除链表的倒数第N个节点

给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.

说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def removeNthFromEnd(head: ListNode, n: int) -> ListNode or None:
    node_pointer2 = head
    for i in range(1, n):
        if node_pointer2.next:
            node_pointer2 = node_pointer2.next
    node_pointer1 = head
    while node_pointer2.next:
        node_pointer1 = node_pointer1.next
        node_pointer2 = node_pointer2.next
    node_pointer3 = head
    if node_pointer3 == node_pointer2:
        head = None
        return head
    if node_pointer3.next == node_pointer2:
        if n == 1:
            node_pointer3.next = None
        else:
            head = node_pointer2
            node_pointer3.next = None
        return head
    if node_pointer3 == node_pointer1:
        head = node_pointer3.next
        node_pointer3.next = None
        return head
    while node_pointer3.next is not node_pointer1:
        node_pointer3 = node_pointer3.next
    node_pointer3.next = node_pointer1.next
    node_pointer1.next = None
    return head


if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node1.next = node2
    print(removeNthFromEnd(node1, 2))
