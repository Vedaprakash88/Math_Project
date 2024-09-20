students = ["Paul", "Erin", "Connie", "Moira"]

for student in range(0, len(students)):
    if student == 2:
        break
    else:
        print(students[student])

    print("Counter is " + str(student))

print("Program Complete")
########################################################################################################
Adv_Prog = ["Ved", "Ashish", "Rohit", "Mustafa", "Asim", "kapil"]

for student in range(0, len(Adv_Prog)):
    if student == 3:
        print("Code has been broken")
        continue
    else:
        print(Adv_Prog[student])

    print("Counter is " + str(student))


print("Program Complete")
#############################################################################3
var1 = list(range(0, 10, 3))
x = 0
while x < len(var1):
    print(var1[x])
    x += 1

##################################################################################
class A:
    def __init__(self, a):
        self.a = a

    # adding two objects
    def __add__(self, o):
        return self.a + o.a


ob1 = A(1)
ob2 = A(2)
ob3 = A("Geeks")
ob4 = A("For")

print(ob1 + ob2)
print(ob3 + ob4)


class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # adding two objects
    def __add__(self, other):
        return self.a + other.a, self.b + other.b

#########################################################################
Ob1 = Complex(1, 2)
Ob2 = Complex(2, 3)
Ob4 = Ob1 + Ob2
print(Ob4)

####################################################################

var1 = list(range(0, 11, 3))
print(var1)

###################################################################

lst1 = [-2, 8, 1, -1, 5]
def norm(lst):
    lst_n = 10 * ((lst - min(lst1)) / (max(lst1) - min(lst1)))
    return lst_n

norm_list = map(norm, lst1)
print((list(norm_list)))

#OR

l = [-2, 8, 1, -1, 5]

min_value = min(l)
max_value = max(l)

l2 = map(lambda item: 10 * ((item - min_value) / (max_value - min_value)), l)

print(list(l2))

#######################################################################


def check(letter):
    list_of_vowels = ['a', 'e', 'i', 'o', 'u']
    if letter in list_of_vowels:
        return True
    else:
        return False


letters = ['u', 'a', 'q', 'c', 'i', 'd', 'z', 'p', 'e']
filtered_object = filter(check, letters)
print("The type of returned object is: ", type(filtered_object))
filtered_list = list(filtered_object)
print("The list of vowels is: ", filtered_list)
######################################################################

class FirstClass:
    def __init__(self, name):
        self.name = name

    def details(self):
        print(self.name)

    def __add__(self, other):
        if isinstance(other, FirstClass):
            self.name += other.name
        return self

    def __str__(self):
        return self.name + ' is the value'

    def __eq__(self, other):
        if isinstance(other, FirstClass):
            return self.name == other.name
        return False

    def __hash__(self):
        return hash(self.name)


class SecondClass(FirstClass):
    def __init__(self, name, age = 20):
        super().__init__(name)
        self.age = age

obj1 = FirstClass('xyz')
print(obj1.name)
obj2 = FirstClass('abc')
print(obj2.name)
print(obj1.name+obj2.name)


obj1.details()

obj3 = SecondClass('klm', 111)
obj3.details()

print(type(obj3) is FirstClass)
print(isinstance(obj3, SecondClass))

obj4 = obj1 + obj2

obj4.details()


value = FirstClass('abc')
def f(value):
    value.name = 'xyz'

f(value)

print (value)

s1 = {FirstClass('abc'), FirstClass('abc')}

print(len(s1))

#print(len(s1))
##############################################################################################
def bubble_sort(lst):
    num = len(lst1)

    for i in range(num):
        for j in range(num-1):
            val1 = lst[j]
            val2 = lst[j+1]
            if val1 > val2:
                lst[j+1], lst[j] = lst[j], lst[j+1]

lst1 = [500, 10, 99, 3, 2, 2, 105, 88, 12, 14, 15, 16, 15, 5, 10, 99, 3, 2, 2, 105, 88, 12, 14, 15, 16, 15]
bubble_sort(lst1)
print(lst1)
###########################################################################################
class FirstClass:
    def __init__(self, name):
        self.__name = name

    def details(self):
        print(self.__name)


obj1 = FirstClass('xyz')
obj1.details()


print(obj1.__name)
obj2 = FirstClass('abc')
print(obj2.__name)