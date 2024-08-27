# DemoLoop.py

value = 5
while value > 0:
    print(value)
    value -= 1

print("---for in 루프---")
lst = [10,20,30]
for i in lst:
    print("Item:{0}".format(i))

print("---range()---")
lst = list(range(1,11))
print(lst)
print([i**2 for i in lst if i  > 5])
print(list(range(2000, 2025)))
print(list(range(1,32)))

print("---필터링 함수---")
lst = [10,25,30]
iterL = filter(None, lst)
for item in iterL:
    print(item)

print("---필터링 함수 사용---")
def getBiggerThan20(i):
    return i > 20

lst = [10,25,30]
iterL = filter(getBiggerThan20, lst)
for item in iterL:
    print(item)

print("---람다 함수 사용---")
iterL = filter(lambda x:x>20, lst)
for item in iterL:
    print(item)