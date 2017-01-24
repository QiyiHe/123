
# people = {
#     'Alice' :{
#         'phone': '2341',
#         'addr': 'Foo Drive'
#     },
#
#     'Beth':{
#         'phone': '9102',
#         'addr' :'Bar Street'
#     },
#
#     'Cecil':{
#         'phone':'3158',
#         'addr' :'Baz Avenue'
#     }
# }
#
# # labels = {
# #     'phone' : 'phone number',
# #     'addr' : 'address'
# # }
#
# name = raw_input('Name: ')
#
# request = raw_input('Phone number (p) or address (a)?')
#
# if request == 'p': key = 'phone'
# if request == 'a': key = 'addr'
#
# if name in people: print name, key, people[name][key]
# else: print 'No Found'
#
# def store(data, full_name):
#     names = full_name.split()
#     if len(names)== 2: names.insert(1, '')
#     labels = 'first', 'middle','last'
#     for label, name in zip(lables, names):
#         people = lookup(data, label, name)
#         if people:
#             people.append(full_name)
#         else:
#             data[label][name] = [full_name]
# #
#
# def hello(name, greeting = 'Hello', punctuation = '!'):
#     print '%s, %s%s' % (greeting,name,punctuation)
#
# print hello('hi',greeting,'hi')

# def hello(x,y):
#
#     return x+y
#
# print hello('aasdads',' bw2')
#
# def add(x,y):
#     return x+y
# def minus (x,y):
#     return x-y
# def multi(x,y):
#     return x*y
# def divide(x,y):
#     return x/y
#
# number1=int (raw_input('enter the first number:'))
# number2 = int (raw_input('enter the second number:'))
# method = raw_input('choose a method, enter the mark:')
# if method == '+': print add(number1,number2)
# elif method == '-': print minus(number1,number2)
# elif method == '*': print multi(number1,number2)
# elif method == '/': print divide(number1,number2)
# else: print 'Wrong!!!'

# def factorial(n):
#     result = n
#     for i in range(1,n):
#         result *= i
#     return result
#
# num = int(raw_input("enter the number"))
# print factorial(num)

# __metaclass__ = type
#
# class Person:
#     def setName(self, name):
#         self.name = name
#
#     def getName(self):
#         return self.name
#     def greet(self):
#         return "hello"+ self.name
# foo = Person()
# foo.setName('haha')
# print foo.greet()

# try:
#     x=input('enter the first number')
#     y=input('enter the second number')
#
#     print x/y
# except (ZeroDivisionError, TypeError, NameError):
#     print 'Your numbers are wrong'
# __metaclass__ = type

# class FooBar:
#     def init(self):
#         self.somevar = 42
# f= FooBar()
# print f.somevar

# def checkIndex(key):
#     if not isinstance(key,(int,long)): raise TypeError
#     if key<0: raise IndexError
# class ArithmeticSequence:
#     def __init__(self,start = 0, step=1):
#         self.start = start
#         self.step = step
#         self.changed = {}
#
#     def __getitem__(self, key):
#         checkIndex(key)
#
#         try:return self.changed[key]
#         except KeyError:
#             return self.start +key*self.step
#
#         def __setitem__(self, key, value)::
#         checkIndex(key)
#
#         self.changed[key] =value
#
# class Rectangle:
#     def __init__(self):
#         self.width = 0
#         self.height = 0
#     def setSize(self, size):
#         self.width, self.height = size
#     def getSize(self):
#         return self.width, self.height
#
# r = Rectangle()
# r.width = 10
# r.height = 5
# print r.getSize()
#
# class Square(Rectangle):
#     def __init__(self):
#         self.width = 0
#         self.height = 0
#
# a = Square()
# a.width = 100
# a.height = 10
# print a.setSize(10)

# class Rectangle:
#     def __init__(self):
#          self.width = 0
#          self.height = 0
#     def __setattr__(self, name, value):
#         if name == 'size':
#             self.width, self.height = value
#         else:
#             self.__dict__[name] = value
#     def __getattr__(self, name):
#         if name == 'size':
#             return self.width, self.height
#         else:
#             raise AttributeError
#
# class Fibs:
#     def __init__(self):
#         self.a=0
#         self.b=1
#     def next(self):
#         self.a, self.b = self.b, self.a+self.b
#         return self.a
#     def __iter__(self):
#         return self
# fibs = Fibs()
# for f in fibs:
#     print f
#     if f>100:
#
#         break
#
# class Dengchashulie():
#     def __init__(self):
#         self.start = 0
#         self.step = 1
#     def next(self):
#         self.start += self.step
#         return self.start
#
#     def __iter__(self):
#         return self
#
# a = Dengchashulie()
#
# for i in a:
#     if i >10: break
#     print i

# def flatten(nested):
#     try:
#         try: nested +''
#         except TypeError: pass
#         else: raise TypeError
#         for sublist in nested:
#             for element in flatten(sublist):
#                 yield element
#     except TypeError:
#         yield nested
# nested = [[1,2],3,[4,5],[6]]
# print list(flatten(nested))


# Eight Queen Problem
# def conflict(state, nextX):
#     nextY = len(state)
#     for i in range(nextY):
#         if abs(state[i]-nextX) in (0,nextY-i):
#             return True
#     return False
#
# def queens(num = 8,state = ()):
#     for pos in range(num):
#         if not conflict(state, pos):
#             if len(state) == num -1:
#                 yield(pos,)
#             else:
#                 for result in queens(num, state +(pos,)):
#                  yield (pos,)+result
# print list(queens(8))
# def prettyprint(solution):
#     def line(pos, length = len(solution)):
#         return'.'*(pos)+'x'+'.'*(length-pos-1)
#     for pos in solution:
#         print line(pos)
#
# import random
# prettyprint(random.choice(list(queens(8))))

# from random import randrange
#
# num = input('How many dice?')
# sides = input('How many sides per dice?')
# sum = 0
#
# for i in range(num): sum += randrange(sides) +1
# print 'the result is', sum


import sys, shelve
#
# def store_person(db):
#     pid = raw_input('Enter the Uniqur ID:')
#     person = {}
#     person['name'] = raw_input('Enter the name:')
#     person['age'] = raw_input('Enter the age:')
#
#     db[pid] = person
#
# def lookup_person(db):
#     pid = raw_input('Enter the ID number')
#     field = raw_input('What would you like to know(name,age)')
#     field = field.strip().lower()
#     print field.capitalize() + ':',\
#         db[pid][field]
#
# def print_help():
#     print 'the available commands are:'
#     print 'store:stores information about a person'
#     print 'look up'
#     print 'quit'
#     print '?'
#
# def enter_command():
#     cmd = raw_input()



# f = open('D:\hello.txt','w')
# f.write('hello world\n')
# f.write('hahahaha\n')
# f.write('This is the third hang')
# f.close()
#
# f = open('D:\hello.txt','r')
# # # print f.read(3)
# # print '+++'
# # print f.read()
# # f.close()
#
# for i in f.readlines():
#     print i
#



