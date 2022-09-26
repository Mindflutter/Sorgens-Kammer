from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """ Add two numbers given as linked lists
    Reference: https://leetcode.com/problems/add-two-numbers/ """
    result_node = next_node = ListNode()
    carry = 0

    while l1 or l2 or carry:
        current_sum = 0
        if l1:
            current_sum += l1.val
            l1 = l1.next
        if l2:
            current_sum += l2.val
            l2 = l2.next
        if carry:
            current_sum += 1

        if current_sum >= 10:
            next_node.val = current_sum % 10
            carry = 1
        else:
            next_node.val = current_sum
            carry = 0

        if any([l1, l2, carry]):
            next_node.next = ListNode()
            next_node = next_node.next

    return result_node


n3 = ListNode(val=9)
n2 = ListNode(val=9, next=n3)
n1 = ListNode(val=9, next=n2)

k3 = ListNode(val=9)
k2 = ListNode(val=9, next=k3)
k1 = ListNode(val=9, next=k2)

res = addTwoNumbers(n1, k1)

while res:
    print(res.val)
    res = res.next

