# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        copy = ListNode()
        head = copy
        while list1 != None and list2!=None:
            if list1.val<list2.val:
                head.next = list1
                head = head.next
                list1= list1.next
            else:
                head.next = list2
                head = head.next
                list2 = list2.next
        while list1!=None:
            head.next = list1
            head = head.next
            list1= list1.next
        while list2!=None:
            head.next = list2
            head = head.next
            list2 = list2.next
        return copy.next

        
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        n = len(lists)
        ll1 = ListNode()
        ll1=ll1.next
        for i in range(0,n):
            ll2  = lists[i]
            ll1 = self.mergeTwoLists(ll1,ll2)
        return ll1
