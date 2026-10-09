"""
给你单链表的头节点 head,请你反转链表,并返回反转后的链表。

head
|
1 ——> 2 ——> 3 ——> 4 ——> 5
"""

# 力扣后台：数组转链表函数
def array_to_linked(arr):
    if not arr:
        return None
    dummy = ListNode()       # 哑节点
    tail = dummy
    for num in arr:
        tail.next = ListNode(num) # 循环：造新节点，接在后面
        tail = tail.next
    return dummy.next         # 返回真正的头节点（节点1）


#____________________________________________
class ListNode:
    def __init__ (self,val=0,next = None):
        self.val = val
        self.next = None

def solution1(head: ListNode) -> ListNode:
    pre = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt
    return pre