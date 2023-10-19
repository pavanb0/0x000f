# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        arr = [] 
        cur = head
        while cur:
            arr.append(cur)
            cur = cur.next 
        lenght = len(arr)-1

        lef , rig = 0 ,lenght 
        last = head
        while lef<rig:
            arr[lef].next = arr[rig]
            lef +=1

            if lef == rig:
                last = arr[rig]
                break
            
            arr[rig].next = arr[lef]
            rig -= 1
            last = arr[lef]
        if last:
            last.next = None 

        


        
        
        