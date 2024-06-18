# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    s1, s2 = '', ''

    while l1:
        s1 += str(l1.val)
        l1 = l1.next
    
    while l2:
        s2 += str(l2.val)
        l2 = l2.next
    
    s1 = s1[::-1]
    s2 = s2[::-1]

    result_str = str(int(s1) + int(s2))[::-1]
    
    result_list = ListNode()
    result = result_list
    for k in result_str:
        result_list.next = ListNode(k)
        result_list = result_list.next

    return result.next

def main():
    l1, l2 = ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4)))
    result2 = addTwoNumbers(l1, l2)
    print(result2)

if __name__ == "__main__":
    main()





