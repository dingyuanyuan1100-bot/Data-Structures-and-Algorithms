class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
    def ListNode_tow(self,list1: ListNode,list2: ListNode) -> ListNode:

       #注意看这个部分
        start = ListNode()
        npm = start
        while list1 and list2:
            if list1.val<=list2.val:
                npm.next = list1
                list1 = list1.next
            else:
                npm.next = list2
                list2 = list2.next
        npm.next = list1 if list1 else list2
        return start.next