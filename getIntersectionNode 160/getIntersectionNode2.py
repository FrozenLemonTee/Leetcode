"""
160. 相交链表

编写一个程序，找到两个单链表相交的起始节点。

如下面的两个链表：

在节点 c1 开始相交。



示例 1：

输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Reference of the node with value = 8
输入解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。



示例 2：

输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
输出：Reference of the node with value = 2
输入解释：相交节点的值为 2 （注意，如果两个链表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。



示例 3：

输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
输出：null
输入解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
解释：这两个链表不相交，因此返回 null。



注意：

    如果两个链表没有交点，返回 null.
    在返回结果后，两个链表仍须保持原有的结构。
    可假定整个链表结构中没有循环。
    程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。


"""

from DSAA.data_structure.basic.LeetcodeNode import ListNode


def getIntersectionNode(head_a: ListNode, head_b: ListNode) -> ListNode or None:
    dummy1 = ListNode("NULL", head_a)
    dummy2 = ListNode("NULL", head_b)
    if head_a and head_b:
        pa = dummy1
        pb = dummy2
        count = 0
        flag = 0
        while pa.next or pb.next:
            while pa.next and pb.next:
                pa = pa.next
                pb = pb.next
                if not pa.next:
                    flag = 1
                if not pb.next:
                    flag = 2
            if not pa.next and not pb.next:
                if pa != pb:
                    return
                else:
                    break
            if pa.next:
                pa = pa.next
            if pb.next:
                pb = pb.next
            count += 1
        pa = dummy1
        pb = dummy2
        for i in range(0, count):
            if flag == 1:
                pb = pb.next
            else:
                pa = pa.next
        while pa != pb:
            pa = pa.next
            pb = pb.next
        return pa


if __name__ == "__main__":
    cross = ListNode(7, ListNode(8, ListNode(9, ListNode(10))))
    list1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, cross))))
    list2 = ListNode(5, ListNode(6, cross))
    print(getIntersectionNode(list2, list1))
    cross2 = ListNode(8, ListNode(4, ListNode(5)))
    list3 = ListNode(4, ListNode(1, cross2))
    list4 = ListNode(5, ListNode(0, ListNode(1, cross2)))
    print(getIntersectionNode(list3, list4))
    cross3 = ListNode(2, ListNode(4, ListNode(5, ListNode(4))))
    list5 = ListNode(2, cross3)
    list6 = ListNode(6, cross3)
    print(getIntersectionNode(list5, list6))
