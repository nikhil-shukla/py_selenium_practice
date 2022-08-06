class Person:

    def __init__(self, name, age,yr):
        self.name = name
        self.age = age
        self.yr = yr
        self.__number = 5  # private member

    def my_func(self):
        print("hello, my name is {}".format(self.name))

    def old_now(self,yr):
        print('old: ',self.age + self.yr)


class Student(Person):

    def __init__(self, school, name, age, yr, buffer):
        super().__init__(name, age, yr)
        self.school = school
        self.buffer = buffer

    def my_func(self):
        super().my_func()
        print(f'my school name is {self.school}')

    def old_now(self,yr,buffer):
        print('old: ',self.age + self.yr+ self.buffer)


p = Person('nik','sfs' ,25)
print(p.name)
p.my_func()

print(p._Person__number) #to access private values

p1 = Student('sfs', 'nik', 25,2,6)
print(p1.school)
p1.my_func()
p1.old_now(5,10)

p2 = Student('gps', 'shaily', 25,6 ,2)
print(p2.school)
p2.my_func()
p2.old_now(20,5)


class X(object):
    def __init__(self, a):
        self.num = a

    def doubleup(self):
        self.num *= 2


class Y(X):
    def __init__(self, a):
        X.__init__(self, a)

    def tripleup(self):
        self.num *= 3


obj = Y(4)
print(obj.num)

obj.doubleup()
print(obj.num)

obj.tripleup()
print(obj.num)


class Employee:

    # Initializing
    def __init__(self):
        print('Employee created')

    # Calling destructor
    def __del__(self):
        print("Destructor called")


def Create_obj():
    print('Making Object...')
    obj = Employee()
    print('function end...')
    return obj


print('Calling Create_obj() function...')
obj = Create_obj()
print('Program End...')


# Python program to illustrate destructor
class Employee:

    # Initializing
    def __init__(self):
        print('Employee created.')

    # Deleting (Calling destructor)
    def __del__(self):
        print('Destructor called, Employee deleted.')


obj = Employee()