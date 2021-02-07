from DSAA.data_structure.basic.LeetcodeNode import ListNode
from Leetcode.mergeKLists.mergeKLists02 import mergeKLists

if __name__ == "__main__":
    test = [ListNode(1, ListNode(3, ListNode(5))), ListNode(1, ListNode(3, ListNode(5))), ListNode(1, ListNode(3, ListNode(5)))]
    print(mergeKLists(test))
    q1 = ListNode(2, ListNode(5, ListNode(8, ListNode(9))))
    q2 = ListNode(4, ListNode(8, ListNode(11)))
    q3 = ListNode(7)
    test2 = [q1, q2, q3]
    print(mergeKLists(test2))
