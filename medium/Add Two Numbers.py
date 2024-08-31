class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def find_last (self,first):
        temp = first
        back_pointer =first
        while (temp.next != None):
            temp =temp.next
            back_pointer =temp
        return back_pointer
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first_int =0
        l1_first = l1
        counter=0
        while l1_first != None:
            first_int+= l1_first.val * (10 ** counter)
            counter +=1
            l1_first = l1_first.next
        counter =0
        second_int =0
        l2_first = l2
        while l2_first != None:
            second_int+= l2_first.val * (10 ** counter)
            counter+=1
            l2_first = l2_first.next
        
        
        sum =first_int +second_int
        first_answer= ListNode (val=0 ,next=None)
        counter =0
        while sum >0:
            mod = sum%10
            sum = sum//10
            if(counter == 0):
                first_answer.val =mod
            else:
                node = self.find_last(first_answer)
                node.next = ListNode(val=mod,next=None)
                
            counter+=1
        return first_answer
    
   
        
        


