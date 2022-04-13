class LinkNode:

    def __init__(self, value=0, next_=None):
        self.value = value
        self.next = next_

    def __str__(self):
        return str(self.value)

    def print(self):
        node = self
        vals = []
        while node:
            vals.append(node.value)
            node = node.next

        print('->'.join([str(v) for v in vals]))
