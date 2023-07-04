import numpy as np


a = np.random.rand(4)
print(a)
b = len(a)/2-1
print(b)
print(a[:int(len(a)/2)])
print(a[int(len(a)/2):])

print('a' in 'ab')
print('c' in 'ab')
print('a' == 'A')

a = ['a', 'B']
print('b' not in a)

a = 'a-b'.split("-")
print(a[1])

print(int('3'))

a = {}
a['x'] = 100
print(a)
print(a['x'])

def A():
    print('b')
    return 'b'
A()
print(A())

a = 'abcdefg'
print(a[:4])
print(a[4:])

class Thing():
    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        return str(self.value)


arr = np.array([1,'b','c','asd', Thing(7)])
arr2 = np.chararray(10)
arr[1] = 1
print(arr[1])
for item in arr:
    print(item)

for item in arr2:
    print(item)

print(arr)
print(arr2)
a = np.array([1,2,3])
a = np.zeros(3)
print(a[-1])

print(list(range(10))[7:4:-2])
a = [1,2,3]
b = [-1,2,3]
c = [a,b]
print(map(lambda a: (a<0).all(), c))

a = np.array([0,0])
b = a
b[0] = 5
print(a)
print(b)


a = np.array([[1,2],[3,4]])
b = np.array([1,0])
print(a[[1,0]])

a = np.array([2,-2])
b = np.sign(a)
print(a)
print(b)

a = np.zeros((2,2))
a[0,1] = 1
print(a[0])

class Person():
    __slots__ = 'a', 'b'
    def __init__(self, a: str, b: int):
        self.a = a
        self.b = b

    

p = Person('a', 2)
print(p.a)
print(p.b)
p.b = 'v'
print(p.b)


print(eval('True'))