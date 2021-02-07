"""
234. 回文链表

请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false

示例 2:

输入: 1->2->2->1
输出: true

进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

"""

# Definition for singly-linked list.
from DSAA.data_structure.basic.LeetcodeNode import ListNode

import math
from collections import deque


def isPalindrome(head: ListNode) -> bool:
    tmp = deque([])
    dummy = ListNode("NULL", head)
    node_pointer = dummy
    count = 1
    while node_pointer.next:
        tmp.append((node_pointer.next.val, count))
        node_pointer = node_pointer.next
        count += 1
    while len(tmp) >= 2:
        if tmp[-1][0] == tmp[0][0]:
            tmp.popleft()
            tmp.pop()
        else:
            break
    return not tmp or (len(tmp) == 1 and tmp[0][1] == math.ceil(count / 2))


if __name__ == "__main__":
    test = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
    print(isPalindrome(test))
    test2 = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))
    print(isPalindrome(test2))
    test3 = ListNode(1, ListNode(2, ListNode(2, ListNode(2, ListNode(1)))))
    print(isPalindrome(test3))
