class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    @staticmethod
    def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
        ptr = l1
        ptr2 = l2
        sol = s = ListNode(None)
        carry = 0

        while True:
            if ptr == None:
                s.val = ptr2.val + carry
            elif ptr2 == None:
                s.val = ptr.val + carry
            else:
                s.val = ptr.val + ptr2.val + carry
                
            if s.val >= 10:
                carry = 1
                s.val = s.val - 10
            else:
                carry = 0
            
            if ptr != None:
                ptr = ptr.next
            if ptr2 != None:
                ptr2 = ptr2.next
            
            if ptr or ptr2:
                s.next = ListNode(None)
                s = s.next
            elif carry == 1:
                s.next = ListNode(1)
                break
            else:
                break
        
        return sol

n = ListNode(5)
m = ListNode(5)

loop = Solution.addTwoNumbers(m,n)

while loop:
    print(str(loop.val), end = " ")
    if loop.next != None:
        print(" -> ", end = " ")
    loop = loop.next