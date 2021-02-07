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


def isPalindrome(head: ListNode) -> bool:
    def reverse(head1: ListNode) -> ListNode or None:
        pre = None
        cur = head1
        while cur:
            last = cur.next
            cur.next = pre
            pre = cur
            cur = last
        return pre

    def findMidNode(head2: ListNode) -> ListNode or None:
        dummy = ListNode("NULL", head2)
        slow = fast = dummy
        while fast:
            for i in range(0, 2):
                fast = fast.next
                if not fast:
                    break
            slow = slow.next
        return slow

    if not head or not head.next:
        return True
    else:
        p_last = reverse(findMidNode(head))
        p_pre = head
        while p_pre and p_last:
            if p_pre.val == p_last.val:
                p_pre = p_pre.next
                p_last = p_last.next
            else:
                return False
    return True


if __name__ == "__main__":
    test = ListNode(1, ListNode(2, ListNode(2, ListNode(1, ListNode(3)))))
    print(isPalindrome(test))
    test2 = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
    print(isPalindrome(test2))
    print(isPalindrome(ListNode(5)))
    print(isPalindrome(ListNode(1, ListNode(2))))
