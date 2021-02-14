class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


class Solution(object):
    """
    https://leetcode.com/problems/linked-list-cycle-ii/discuss/44783/Share-my-python-solution-with-detailed-explanation
    """
    def findCycleStart(self, head):
        try:
            fast = head.next
            slow = head
            while fast is not slow:
                fast = fast.next.next
                slow = slow.next
        except AttributeError:
            return None

        slow = slow.next
        while head is not slow:
            head = head.next
            slow = slow.next
        return head