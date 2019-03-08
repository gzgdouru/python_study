'''
实现访问者模式
'''


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
        return self.visit(node.left) - self.visit(node.right)

    def visit_mul(self, node):
        return self.visit(node.left) * self.visit(node.right)

    def visit_div(self, node):
        return self.visit(node.left) / self.visit(node.right)

    def visit_add(self, node):
        return self.visit(node.left) + self.visit(node.right)

    def visit_negate(self, node):
        return -node.operand.value


class StackCode(NodeVisitor):
    def generate_code(self, node):
        self.instructions = []
        self.visit(node)
        return self.instructions

    def visit_number(self, node):
        self.instructions.append(("PUSH", node.value))

    def binop(self, node, instruction):
        self.visit(node.left)
        self.visit(node.right)
        self.instructions.append((instruction,))

    def visit_add(self, node):
        self.binop(node, 'ADD')

    def visit_sub(self, node):
        self.binop(node, 'SUB')

    def visit_mul(self, node):
        self.binop(node, 'MUL')

    def visit_div(self, node):
        self.binop(node, 'DIV')

    def unaryop(self, node, instruction):
        self.visit(node.operand)
        self.instructions.append((instruction,))

    def visit_negate(self, node):
        self.unaryop(node, "NEG")


if __name__ == "__main__":
    # Representation of 1 + 2 * (3 - 4) / 5
    # t1 = Sub(Number(3), Number(4))()
    # t2 = Mul(Number(2), t1)()
    # t3 = Div(t2, Number(5))()
    # t4 = Add(Number(1), t3)()
    # print(t4.value)
    # print(Negate(Number(3))().value)

    e = Evaluator()
    t1 = Sub(Number(3), Number(4))
    t2 = Mul(Number(2), t1)
    t3 = Div(t2, Number(5))
    t4 = Add(Number(1), t3)
    print(e.visit(t4))
    print(e.visit(Negate(Number(3))))

    s = StackCode()
    print(s.generate_code(t4))
