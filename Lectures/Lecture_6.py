def mygenerator():
    print('First item')
    yield 10

    print('Second item')
    yield 20

    print('Last item')
    yield 30


gen = mygenerator()


#####################################################################################################
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError('A problem occurred')
    return a / b


try:
    print(divide(10, 0))
except ZeroDivisionError as e:
    print(e, "Cannot divide a value by Zero")
finally:
    print('finally done')


#####################################################################################################
def fibonacci(n):
    if n == 0:
        print("No Sequence with zero")
    else:
        for i in range(0, n, 1):
            x = (n - 1) + (n - 2)
            print(x)


#####################################################################################################
def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        yield 0
        yield 1
        a = 0
        b = 1
        for i in range(0, n, 1):
            a, b = b, a + b
            yield b

    result = []
    result.append(b)
    return result


fib = fibonacci(10)

for i in fib:
    print(i)


#############################################################################################
# Decorators

def decorator_factory_fun(d):
    def decorator_fun(func):
        def inner(x, y):
            return func(x + d, y)

        return inner

    return decorator_fun


@decorator_factory_fun(d=10)
def mul(a, b):
    return a * b


print(mul(2, 3))

################################################################################################
# Decorators

operators = {
    'add': lambda a, b: a + b,
    'sub': lambda a, b: a - b
}


def evaluate(expr):
    if type(expr) is float or type(expr) is int:
        return expr

    operand1, operator, operand2 = expr

    const1 = evaluate(operand1)
    const2 = evaluate(operand2)

    if operator in operators:
        f = operators[operator]
        f(const1, const2)
    else:
        print('unknown operator')
        return 0
#################################################################################
operators = {
    'add': lambda a, b: a + b,
    'sub': lambda a, b: a - b
}


class UnknownOperatorError(NameError):
    pass

def evaluate(expr):
    if type(expr) is float or type(expr) is int:
        return expr

    operand1, operator, operand2 = expr

    const1 = evaluate(operand1)
    const2 = evaluate(operand2)

    if operator in operators:
        f = operators[operator]
        return f(const1, const2)
    else:
        raise UnknownOperatorError(f"I don't know {operator}")


def op(name):
    def decorator_fun(func):
        operators[name] = func
        return func
    return decorator_fun

#from evaluator import evaluate, op # Was written by Prof. in different python file, so calling here


@op(name='mul')
def mul(a, b):
    return a * b


@op(name='div')
def div(a, b):
    return a / b


t = (2.5, 'mul', ((10, 'div', 2), 'add', 7))

print(evaluate(t))

####################################################################
#Unit Testing

operators = {
    'add': lambda a, b: a + b,
    'sub': lambda a, b: a - b
}


class UnknownOperatorError(NameError):
    pass

def evaluate(expr):
    if type(expr) is float or type(expr) is int:
        return expr

    operand1, operator, operand2 = expr

    const1 = evaluate(operand1)
    const2 = evaluate(operand2)

    if operator in operators:
        f = operators[operator]
        return f(const1, const2)
    else:
        raise UnknownOperatorError(f"I don't know {operator}")


def op(name):
    def decorator_fun(func):
        operators[name] = func
        return func
    return decorator_fun

#Test-Code

import unittest
#from evaluator import evaluate, UnknownOperatorError # Was written by Prof. in different python file, so calling here


class TestEvaluator(unittest.TestCase):

    def test_basic_add(self):
        self.assertEqual(12, evaluate((5, 'add', 7)))

    def test_basic_sub(self):
        self.assertEqual(0, evaluate((6, 'sub', 6)))

    def test_constant(self):
        self.assertEqual(0, evaluate(6))

    def test_raise_unknown_operator(self):
        with self.assertRaises(UnknownOperatorError) as context:
            evaluate((5, 'add', 6))

        self.assertTrue(context.exception)


if __name__ == '__main__':
    unittest.main()
