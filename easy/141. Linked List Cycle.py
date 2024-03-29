from typing import Optional
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        if head.next == None:
            return False
        num = 0
        while(1):
            if head.next == None:
                return False
            head = head.next
            num += 1
            if num > 10000:
                return True
        return False