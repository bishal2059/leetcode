# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeNodes(self, head: ListNode) -> ListNode:
        sum_value = 0
        current_node = head.next
        new_head = ListNode(0,None)
        new_current_head = new_head
        while(current_node != None):
            sum_value += current_node.val
            if(current_node.val == 0):
                new_current_head.val = sum_value
                if current_node.next != None:
                    next = ListNode(0,None)
                    new_current_head.next = next
                    new_current_head = next
                sum_value = 0
            current_node = current_node.next
        # print(new_head)
        return new_head                



        