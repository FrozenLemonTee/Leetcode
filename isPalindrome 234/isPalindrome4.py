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


class solution:
    def __init__(self):
        self.p = None

    def isPalindrome(self, head: ListNode) -> bool:
        self.p = head

        def recursion(node1: ListNode) -> bool:
            if node1.next:
                return recursion(node1.next) and isEqual(node1)
            else:
                return isEqual(node1)

        def isEqual(node2: ListNode) -> bool:
            if self.p.val == node2.val:
                self.p = self.p.next
                return True
            else:
                self.p = self.p.next
                return False

        if head:
            return recursion(head)
        else:
            return True


if __name__ == "__main__":
    test = ListNode(1, ListNode(2, ListNode(2, ListNode(1, ListNode(3)))))
    s = solution()
    print(s.isPalindrome(test))
    test2 = ListNode(2, ListNode(1, ListNode(1, ListNode(2))))
    print(s.isPalindrome(test2))
