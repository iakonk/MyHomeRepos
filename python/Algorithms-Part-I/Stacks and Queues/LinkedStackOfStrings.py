class Node(object):
    def __init__(self, item, next):
        self.item = item
        self.next = next


class LinkedStackOfStrings(object):
    def __init__(self, first=None):
        self.first = first

    def isEmpty(self):
        return self.first is None

    def push(self, item):
        old_first = self.first
        first = None(item, old_first)
        self.first = first

    def pop(self):
        item = self.first
        self.first = self.first.next
        return item