class LinkNode:

    def __init__(self, value=0, next_=None):
        self.value = value
        self.next = next_

    def __str__(self):
        return str(self.value)
