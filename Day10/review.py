"""def f(x):
    return 2 * x + 3

print f(2)
print f(3 + 4 * 6)
print(f(f(6)))

v = 89
print f(v)

def gerGreater(x1, x2):

    if x1 >= x2:
        return x1
    else:
        return x2

x = float(raw_input('Enter first number '))
y = float(raw_input('Enter second number '))

print(gerGreater(x, y))

def conCat():

    word = raw_input('Enter a string ')
    return word + word
    
print conCat()

def threeMore(x1, x2, x3):

    value = (x1 * x2 * x3) + 3
    print value

threeMore(2, 3, 4)

l = []

k = list()

j = [1,2,3,4,5,6,7,8,9,10]

print "The list before insert"
print "l =", l
print "k =", k
print "j =", j

l.insert(0,'h')
k.insert(0,'a')
j.insert(5,12)

print("The list after insert")
print "l =", l
print "k =", k
print "j =", j

l.pop()
k.pop()
j.pop()

l = [2,3,6,7,8]
k = [4,1,5,12,13]

print("The list after insert')
print "l =", l
print "k =", k
print "j =", j

i = 1
while i <= 10:
    print i
    i += 1

i = 1
while i <= 20:
    print i
    i += 1

i = 1
while i <= 20:
    if i % 2 == 0:
        print i
        i += 1
    
while i <= 20:
    if i % 2 == 1:
        print i
        i += 1

v = ""
while v != "hello":
    v = raw_input("Enter a string ")

for i in range(1,11):
    print i
for i in range(1,21):
    print i
for i in range(2,21,2):
    print i
for i in range(1,21):
    if i % 2 == 0:
        print i
for i in "This is a string":
    print i

h = []

for i in range(20):
    h.append(0)

print h, len(h)

h[1] = 1

for i in range(2,20):
    h[i] = h[i-1] + h[i-2]

print h

d = {}
b = dict()
a = {1:2,2:1,3:3,4:5,5:4} 
c = {12:"John Smith",88:"Jane Doe"}

print a[1]

print c[88]

c[72] = "Joe Brown"

print c
"""

class Person:
    def __init__(self,name):
        self.name = name
        self.age = 0
    
    def birthday(self):
        self.age += 1

t = Person("Jane Doe")

print t.name, t.age

s = Person("Roger Sam")

print s.name, s.age

t.birthday()

print t.name, t.age
