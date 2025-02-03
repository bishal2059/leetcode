from typing import Optional, List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
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

def array_to_linked_list(arr: List[int]) -> Optional[ListNode]:
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def linked_list_to_array(head: Optional[ListNode]) -> List[int]:
    arr = []
    current = head
    while current is not None:
        arr.append(current.val)
        current = current.next
    return arr

if __name__ == "__main__":
    arr = [0,3,1,0,4,5,2,0]
    head = array_to_linked_list(arr)
    new_head = Solution().mergeNodes(head)
    result_arr = linked_list_to_array(new_head)
    print(result_arr)
        