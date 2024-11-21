# https://leetcode.com/problems/reverse-linked-list/description/

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# time O(n), mem O(1)
def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    cur = head

    # when cur is null, we've completed the reversal
    while cur:
        next = cur.next # set next before destroying the link
        cur.next = prev # reverse cur's link to prev
        # shift prev and cur to right
        prev = cur
        cur = next

    # at this point, cur points to null, and prev is our new head
    return prev # don't forget the return