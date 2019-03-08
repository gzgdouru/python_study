'''
实现迭代器协议
'''


class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __str__(self):
        return f"Node:{self._value}"

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        yield self
        for ch in self:
            yield from ch.depth_first()


if __name__ == "__main__":
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))

    for ch in root.depth_first():
        print(ch)
