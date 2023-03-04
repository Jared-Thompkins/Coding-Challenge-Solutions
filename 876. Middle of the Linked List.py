class Solution:
    def middleOfLinkedList(self, head):
        length = 0
        start = node = head
        counter = 0

        while start:
            length += 1
            start = start.next

        middle = length // 2

        while node:
            if counter == middle:
                return node
            else:
                counter += 1
                node = node.next
        return None