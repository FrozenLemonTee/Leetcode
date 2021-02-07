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
    # False
    tmp = {}
    dummy = ListNode("NULL", head)
    node_pointer = dummy
    while node_pointer.next:
        if node_pointer.next.val not in tmp.keys():
            tmp.update({node_pointer.next.val: 1})
        else:
            tmp[node_pointer.next.val] += 1
        node_pointer = node_pointer.next
    for num in tmp.keys():
        tmp[num] %= 2
    flag = 0
    for num in tmp.keys():
        if tmp[num] != 0 and flag == 0:
            flag = 1
        elif tmp[num] != 0 and flag == 1:
            return False
    return True


if __name__ == "__main__":
    test = ListNode(1, ListNode(1, ListNode(1)))
    print(isPalindrome(test))
    test2 = ListNode(1, ListNode(2, ListNode(2, ListNode(2, ListNode(1)))))
    print(isPalindrome(test2))
