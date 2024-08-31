class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # create empty link list
        answer= ListNode (val=0 ,next=None)
        # save for return
        answer_first = answer
        # variable for save carry value of each sum
        addition =0
        while (addition !=0 or l1 != None or l2 !=None):
            first_num =0
            # check if first array is not None
            if(l1):
                first_num = l1.val
            second_num = 0
            # check for second array
            if(l2):
                second_num =l2.val
            # do some with carry
            sum =first_num +second_num +addition
            new_value = sum%10
            addition = sum //10
            # create new ListNode with sum value
            answer_first.next = ListNode(val=new_value,next=None)
            answer_first = answer_first.next
            # iterate over lists
            if(l1):
                l1 = l1.next
            if(l2):
                l2 = l2.next
            
        return answer.next

        
            
        
            

        
    
   
        
        


