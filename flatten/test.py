from DSAA.data_structure.basic.LeetcodeNode import DoubleListNode
from Leetcode.flatten.flatten import flatten

if __name__ == "__main__":
    q3 = DoubleListNode(11, next_node=DoubleListNode(12))
    q2 = DoubleListNode(7, next_node=DoubleListNode(8, next_node=DoubleListNode(9, next_node=DoubleListNode(10))), child=q3)
    q1 = DoubleListNode(1,
                        next_node=DoubleListNode(2, next_node=DoubleListNode(3, next_node=DoubleListNode(4, next_node=DoubleListNode(5, next_node=DoubleListNode(6))), child=q2)))
    print(flatten(q1))
