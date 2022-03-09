# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution_1:
    """
    O(2N)
    1st pass: remove duplicates
    2nd pass: make the no_dup_list to linked list
    """
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = {}
        
        while (head):
            if head.val not in seen:
                seen.update({head.val: 1})
            else:
                seen[head.val] += 1
                
            head = head.next
        
        no_dup_list = [k for k, v in seen.items() if v==1]
        if len(no_dup_list) == 0:
            return
        elif len(no_dup_list) == 1:
            return ListNode(no_dup_list[0])
        else:
            # assign both cur and start node as ListNode(no_dup_list[0])
            # and then only move cur node to append next values 
            # then return the start node at the end that did not move the whole time 
            cur = start = ListNode(no_dup_list[0])
            for e in no_dup_list[1:]:
                cur.next = ListNode(e)
                cur = cur.next
            return start
        

class Solution_2:
    """
    O(N)
    Using sentinel node, predecessor, and current head
    """
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # sentinel
        sentinel = ListNode(0, head)

        # predecessor = the last node 
        # before the sublist of duplicates
        pred = sentinel
        
        while head:
            # if it's a beginning of duplicates sublist 
            # skip all duplicates
            if head.next and head.val == head.next.val:
                # move till the end of duplicates sublist
                while head.next and head.val == head.next.val:
                    head = head.next
                # skip all duplicates
                pred.next = head.next 
            # otherwise, move predecessor
            else:
                pred = pred.next 
                
            # move forward
            head = head.next
            
        return sentinel.next