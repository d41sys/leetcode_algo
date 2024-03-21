# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        arr = [] 
        while head != None:
            arr.append(head.val)
            head = head.next
        arr.reverse() 
        res = ListNode(arr[0])
        pointer = res
        for i in range(1,len(arr)):
            temp = ListNode(arr[i])
            pointer.next = temp
            pointer = temp
        return res