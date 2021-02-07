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


def deleteDuplicates(head: ListNode) -> ListNode or None:
    q = ListNode("NULL", head)
    val = {}
    pointer = q
    while pointer.next:
        pointer = pointer.next
        if pointer.val not in val.keys():
            val.update({pointer.val: 1})
        else:
            val[pointer.val] += 1
    q.next = None
    pointer = q
    for num in val.keys():
        if val[num] == 1:
            pointer.next = ListNode(num)
            pointer = pointer.next
    return q.next


if __name__ == "__main__":
    test = ListNode(1, ListNode(1, ListNode(3, ListNode(4, ListNode(4, ListNode(5, ListNode(5)))))))
    print(deleteDuplicates(test))
    test2 = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(5, ListNode(5, ListNode(5)))))))
    print(deleteDuplicates(test2))
