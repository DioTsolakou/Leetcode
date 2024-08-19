# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def merge_two_lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        current = result
        
        while list1 and list2:
            if list1.val > list2.val:
                current.next = list2
                list2 = list2.next
            else:
                current.next = list1
                list1 = list1.next

            current = current.next

        if not list1:
            current.next = list2
        if not list2:
            current.next = list1

        return result.next



def main():
    list1, list2 = ListNode(1, ListNode(2, ListNode(4))), ListNode(1, ListNode(3, ListNode(4)))
    result = Solution.merge_two_lists(Solution, list1, list2)
    print(result)

if __name__ == "__main__":
    main()