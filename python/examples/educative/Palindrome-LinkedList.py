class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def reverse(head):
    prev, curr = None, head
    while curr is not None:
        next_tmp = curr.next
        curr.next = prev
        prev = curr
        curr = next_tmp
    return prev


def find_middle(head):
    slow = fast = head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
    return slow


def is_palindromic_linked_list(head):
    if head is None or head.next is None:
        return True

    middle_node = find_middle(head)
    reverse(middle_node)
    start, end = head, middle_node

    while start is not None and end is not None:
        if start.value != end.value:
            break
        start = start.next
        end = end.next

    reverse(middle_node)

    if start is None or end is None:
        return True

    return False


def reverse(head):
    prev = None
    while (head is not None):
        next = head.next
        head.next = prev
        prev = head
        head = next
    return prev


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)

    print("Is palindrome: " + str(is_palindromic_linked_list(head)))

    head.next.next.next.next = Node(2)
    print("Is palindrome: " + str(is_palindromic_linked_list(head)))


main()
