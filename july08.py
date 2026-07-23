l = [1, 2, 3.14, "Hello", True,]
l.append("Tomorrow")
l.pop(2)
print(l)

s = set()
s.add(1)
s.add(1)
print(s)

d = {1: 'A', 2: 'B', 3: 'C'}
for k, v in d.items():
    print(k, v)


def sutharsan():
    return "Hello"
print(sutharsan())

class sutharsan():
    def __init__(self, i):
        self.i = i

    def sutharsan():
        print(self.i)
        def sutharsan1(self, j):
            print(j)

obj = sutharsan(2)
obj.sutharsan()
obj.sutharsan1(4)

d = {"name": "Sutharsan", 
     "age": 20,
     "salary": 1000000000}

import json
res = json.dumps(d)
print(res)
print(type(res))

with open("july08.json", "r") as file:
    data = json.load(file)
    print(data)
    print(type(data))    