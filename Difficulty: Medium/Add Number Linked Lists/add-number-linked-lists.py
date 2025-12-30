'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def addTwoLists(self, head1, head2):
        
        
        def reverse(head):
            prev = None
            while head:
                nxt = head.next
                head.next = prev
                prev = head
                head = nxt
            return prev
        
        
        head1 = reverse(head1)
        head2 = reverse(head2)
        
        
        dummy = Node(0)
        curr = dummy
        carry = 0
        
        while head1 or head2 or carry:
            val = carry
            if head1:
                val += head1.data
                head1 = head1.next
            if head2:
                val += head2.data
                head2 = head2.next
            
            curr.next = Node(val % 10)
            curr = curr.next
            carry = val // 10
        
        # Reverse the result back
        result = reverse(dummy.next)
        
        # Remove leading zeros
        while result and result.data == 0:
            result = result.next
        
        return result if result else Node(0)

        