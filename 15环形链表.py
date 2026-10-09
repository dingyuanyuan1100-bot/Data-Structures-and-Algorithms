"""
给定一个链表的头节点 head,返回链表开始入环的第一个节点。如果链表无环,则返回null。
如果链表中有某个节点,可以通过连续跟踪 next 指针再次到达,则链表中存在环。为了表示给定链
表中的环,评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置(索引从0开始)。如果
pos是-1,则在该链表中没有环。注意:pos 不作为参数进行传递,仅仅是为了标识链表的实际情
况。
不允许修改 链表。

"""
class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

#我的解法
def solution1(self,head: ListNode) -> bool:
    left=head
    right=head.next
    while right!=left:
        if right == None:
            return False
        right=right.next.next
        left=left.next
    return True

def solution2(self,head: ListNode) -> bool:
    left=head
    right=head
    while right!=None and right.next!=None:
        left=left.next
        right=right.next.next
        if right==left:
            return True
    return False