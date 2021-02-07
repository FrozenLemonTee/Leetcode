"""
83. 删除排序链表中的重复元素

给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:

输入: 1->1->2
输出: 1->2

示例 2:

输入: 1->1->2->3->3
输出: 1->2->3


"""

# Definition for singly-linked list.
from DSAA.data_structure.basic.LeetcodeNode import ListNode


def deleteDuplicates(head: ListNode) -> ListNode:
    q = ListNode("NULL", head)
    node_pointer = q
    if node_pointer.next:
        node_pointer = node_pointer.next
        while node_pointer.next:
            while node_pointer.next and node_pointer.next.val == node_pointer.val:
                node_pointer.next = node_pointer.next.next
            if node_pointer.next:
                node_pointer = node_pointer.next
    return q.next


if __name__ == "__main__":
    test = ListNode(1, ListNode(1, ListNode(1, ListNode(2, ListNode(2, ListNode(3))))))
    print(deleteDuplicates(test))
    test2 = ListNode(1, ListNode(1, ListNode(1, ListNode(1, ListNode(2, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(8))))))))))))))
    print(deleteDuplicates(test2))
