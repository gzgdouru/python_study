'''
不用递归实现访问者模式
'''
import types


class Node:
    pass


class UnaryOperator(Node):
    def __init__(self, operand):
        self.operand = operand


class BinaryOperator(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Add(BinaryOperator):
    def __call__(self, *args, **kwargs):
        return Number(self.left.value + self.right.value)


class Sub(BinaryOperator):
    def __call__(self, *args, **kwargs):
        return Number(self.left.value - self.right.value)


class Mul(BinaryOperator):
    def __call__(self, *args, **kwargs):
        return Number(self.left.value * self.right.value)


class Div(BinaryOperator):
    def __call__(self, *args, **kwargs):
        return Number(self.left.value / self.right.value)


class Negate(UnaryOperator):
    def __call__(self, *args, **kwargs):
        return Number(-self.operand.value)


class Number(Node):
    def __init__(self, value):
        self.value = value


class NodeVisitor:
    def visit(self, node):
        stack = [node]
        last_result = None
        while stack:
            try:
                last = stack[-1]
                if isinstance(last, types.GeneratorType):
                    stack.append(last.send(last_result))
                elif isinstance(last, Node):
                    stack.append(self._visit(stack.pop()))
                else:
                    last_result = stack.pop()
            except StopIteration:
                last_result = stack.pop()
        return last_result

    def _visit(self, node):
        methname = "visit_" + type(node).__name__.lower()
        meth = getattr(self, methname, None)
        if meth is None:
            meth = self.generic_visit
        return meth(node)

    def generic_visit(self, node):
        raise RuntimeError('No {} method'.format('visit_' + type(node).__name__.lower()))


class Evaluator(NodeVisitor):
    def visit_number(self, node):
        return node.value

    def visit_sub(self, node):
        yield (yield self.visit(node.left)) -  (yield self.visit(node.right))

    def visit_mul(self, node):
        yield (yield self.visit(node.left)) * (yield self.visit(node.right))

    def visit_div(self, node):
        yield (yield self.visit(node.left)) / (yield self.visit(node.right))

    def visit_add(self, node):
        yield (yield self.visit(node.left)) + (yield self.visit(node.right))

    def visit_negate(self, node):
        return -node.operand.value


if __name__ == "__main__":
    # e = Evaluator()
    # t1 = Sub(Number(3), Number(4))
    # t2 = Mul(Number(2), t1)
    # t3 = Div(t2, Number(5))
    # t4 = Add(Number(1), t3)
    # print(e.visit(t4))
    # print(e.visit(Negate(Number(3))))

    a = Number(0)
    for n in range(1, 100000):
        a = Add(a, Number(n))
    e = Evaluator()
    e.visit(a)
