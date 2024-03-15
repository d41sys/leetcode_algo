
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lenght = 0
        if head == None or head.next == None:
            return head
        pointer = head
        
        while pointer != None:
            lenght += 1
            pointer = pointer.next
        
        pos = (lenght // 2)
        while(pos > 0):
            head = head.next
            pos -= 1
            
        return head
