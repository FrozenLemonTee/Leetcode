"""
82. 删除排序链表中的重复元素 II

给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

示例 1:

输入: 1->2->3->3->4->4->5
输出: 1->2->5

示例 2:

输入: 1->1->1->2->3
输出: 2->3


"""

# Definition for singly-linked list.
from DSAA.data_structure.basic.LeetcodeNode import ListNode


def deleteDuplicates(head: ListNode) -> ListNode:
    q = ListNode("NULL", head)
    pre = q
    count = 0
    last = pre.next
    if last:
        val = last.val
        while last:
            if last.val == val and count < 2:
                count += 1
            elif last.val != val and count == 2:
                val = last.val
                count = 1
                pre.next = last
            elif last.val != val and count < 2:
                val = last.val
                pre = pre.next
            last = last.next
        if count == 2:
            pre.next = last
    return q.next


if __name__ == "__main__":
    test = ListNode(1, ListNode(1, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5)))))))
    print(deleteDuplicates(test))
    test2 = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(5, ListNode(5)))))))
    print(deleteDuplicates(test2))
