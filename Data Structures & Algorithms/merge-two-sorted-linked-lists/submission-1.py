class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        res = ListNode()
        t = res

        while list1 and list2:
            if list1.val <= list2.val:
                t.next = list1
                list1 = list1.next
            else:
                t.next = list2
                list2 = list2.next
            t = t.next
        if list1:
            t.next = list1
        elif list2:
            t.next = list2
        return res.next