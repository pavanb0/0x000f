class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        out = ListNode()
        dummy = out 
        while list1 and list2:
            if list1.val<list2.val:
                dummy.next = list1
                list1 = list1.next

            else:
                dummy.next = list2
                list2 = list2.next

            dummy = dummy.next

        if not list1:
            dummy.next = list2
        else:
            dummy.next = list1

        return out.next


            
