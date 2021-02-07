"""
25. K 个一组翻转链表

给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。



示例：

给你这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5



说明：

    你的算法只能使用常数的额外空间。
    你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换
"""

from DSAA.data_structure.basic.LeetcodeNode import ListNode


def reverseKGroup(head: ListNode, k: int) -> ListNode:
    def hasKNext(cur_pointer: ListNode) -> bool:
        pointer = cur_pointer
        for i in range(0, k+1):
            if pointer:
                pointer = pointer.next
            else:
                return False
        return True

    # 在hasKNext()为True的范围里使用
    def nextSNode(cur_pointer: ListNode, step: int) -> ListNode:
        pointer = cur_pointer
        for i in range(0, step):
            pointer = pointer.next
        return pointer

    p = ListNode("NULL", head)
    last_pointer = p
    while hasKNext(last_pointer):
        pre_pointer = nextSNode(last_pointer, k+1)
        new_first = nextSNode(last_pointer, k)
        for j in range(k - 1, 0, -1):
            node_pointer = nextSNode(last_pointer, j)
            node_pointer.next.next = node_pointer
        last_pointer.next.next = pre_pointer
        last_pointer.next = new_first
        last_pointer = nextSNode(last_pointer, k)
    return p.next


if __name__ == "__main__":
    test = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(reverseKGroup(test, 2))
