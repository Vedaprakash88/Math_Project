def evaluate(expr):
    if type(expr) is float or type(expr) is int:
        return expr

    operand1, operator, operand2 = expr

    const1 = evaluate(operand1)
    const2 = evaluate(operand2)

    if operator == 'add':
        return const1 + const2
    elif operator == 'div':
        return const1 / const2
    elif operator == 'mul':
        return const1 * const2
    elif operator == 'sub':
        return const1 - const2
    else:
        print('unknown operator')
        return 0
t = (2.5, 'mul', ((10, 'div', 2), 'add', 7))
print(evaluate(t))

##########################################################################################################
t = ((1, 6), ((3, 10), (7, (4, 17))))

sum = 0

def visit(t, visitor):
    if type(t) is float or type(t) is int:
        visitor(t)
    else:
        t1, t2 = t

        visit(t1, visitor)
        visit(t2, visitor)


def sum_visitor(num):
    global sum
    sum += num

visit(t, sum_visitor)
print(sum)

product = 1
def product_visitor(num):
    global product
    product *= num
visit(t, product_visitor)
print(product)
##############################################################################################

t = ((1, 6), ((3, 10), (7, (4, 17))))


def visit(t, visitor, initial):
    if type(t) is float or type(t) is int:
        return visitor(t, initial)
    else:
        t1, t2 = t

        initial = visit(t1, visitor, initial)
        return visit(t2, visitor, initial)


sum = visit(t, lambda value, current: value + current, 0)
print(sum)

product = visit(t, lambda value, current: value * current, 1)
print(product)

is_4_in = visit(t, lambda value, current: current or value == 100, False)
print(is_4_in)
##################################################################################################
my_list = [2.6743,3.63526,4.2325,5.9687967,6.3265,7.6988,8.232,9.6907]

updated_list = map(lambda x: x+1, my_list)
print(updated_list)
print(list(updated_list))
filter_list = list(filter(lambda item: item > 3, my_list))
print(filter_list)
##################################################################################################
car={
    "model" : "mustang",
    "year" : 2001
}
car["model"]

print("model" in car)

myset = {"a", "b", "c"}
myset2 = {"x", "z", "c"}
print(myset)
print(myset & myset2)
print(myset | myset2)
##############################################################################################
from functools import reduce

my_list = [2.6743,3.63526,4.2325,5.9687967,6.3265,7.6988,8.232,9.6907]

updated_list = map(lambda x: x+1, my_list)
print(updated_list)
print(list(updated_list))
filter_list=filter(lambda item: item>3,my_list)
print(list(filter_list))

sum = reduce(lambda aggregated, value: aggregated + value, my_list, 0)

print (sum)