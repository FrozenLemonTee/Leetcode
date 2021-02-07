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


def deleteDuplicates(head: ListNode) -> ListNode or None:
    val = []
    p = ListNode("NULL", head)
    pointer = p
    while pointer.next:
        pointer = pointer.next
        val.append(pointer.val)
    dic = sorted(set(val))
    p.next = None
    pointer = p
    for num in dic:
        pointer.next = ListNode(num)
        pointer = pointer.next
    return p.next


if __name__ == "__main__":
    test2 = ListNode(-1, ListNode(0, ListNode(0, ListNode(0, ListNode(3, ListNode(3))))))
    print(deleteDuplicates(test2))
