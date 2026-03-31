# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            lst = []
            curr = head
            while curr != None:
                lst.append(curr.val)
                curr = curr.next
            
            head = ListNode(lst[-1])
            lst.pop(-1)
            curr = head
            i = len(lst) - 1
            while curr != None:
                if i >= 0:
                    node = ListNode(lst[i])
                    curr.next = node
                    curr = node
                    i -= 1
                else:
                    curr = None
            return head
            
            

        

        