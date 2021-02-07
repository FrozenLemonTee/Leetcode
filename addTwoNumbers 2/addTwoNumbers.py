"""
2. 两数相加

给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807


"""


class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next = None


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    l3 = ListNode(0)
    carry = 0
    node_pointer1 = l1
    node_pointer2 = l2
    node_pointer3 = l3
    node_pointer3.val = (node_pointer1.val + node_pointer2.val + carry) % 10
    if node_pointer1.val + node_pointer2.val + carry > 9:
        carry = 1
    else:
        carry = 0
    node_pointer1 = node_pointer1.next
    node_pointer2 = node_pointer2.next
    while True:
        if not node_pointer1 and not node_pointer2:
            if carry == 1:
                node_pointer3.next = ListNode(1)
            break
        elif node_pointer1 and not node_pointer2:
            node_pointer3.next = ListNode((node_pointer1.val + carry) % 10)
            node_pointer3 = node_pointer3.next
            if node_pointer1.val + carry > 9:
                carry = 1
            else:
                carry = 0
        elif node_pointer2 and not node_pointer1:
            node_pointer3.next = ListNode((node_pointer2.val + carry) % 10)
            node_pointer3 = node_pointer3.next
            if node_pointer2.val + carry > 9:
                carry = 1
            else:
                carry = 0
        else:
            node_pointer3.next = ListNode((node_pointer1.val + node_pointer2.val + carry) % 10)
            node_pointer3 = node_pointer3.next
            if node_pointer1.val + node_pointer2.val + carry > 9:
                carry = 1
            else:
                carry = 0
        if node_pointer1:
            node_pointer1 = node_pointer1.next
        if node_pointer2:
            node_pointer2 = node_pointer2.next
    return l3


if __name__ == "__main__":
    p1 = ListNode(2)
    p2 = ListNode(4)
    p3 = ListNode(3)
    q1 = ListNode(5)
    q2 = ListNode(6)
    q3 = ListNode(4)
    p1.next = p2
    p2.next = p3
    q1.next = q2
    q2.next = q3
    k1 = addTwoNumbers(p1, q1)
    k2 = k1.next
    k3 = k2.next
    print(k1.val, k2.val, k3.val)
