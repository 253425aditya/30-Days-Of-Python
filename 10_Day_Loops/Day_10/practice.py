for i in range(10,0,-1):
    print(i)

for i in range(1,8):
    for i in range(i):
        print('#',end="")
    print()


print("\n\n\n\n")

for i in range(10):
    for j in range(10):
        print('# ',end="")
    print()

print("\n")

for i in range(11):
    print(f"{i} x {i} = {i*i}")

print("\n")

lst = ['Python', 'Numpy','Pandas','Django', 'Flask']
for i in lst:
    print(i)

print("\n")

for i in range(101):
    if i%2==0:
        print(i)

print("\n")

for i in range(101):
    if i%2!=0:
        print(i)

print("\n")
sum = 0
for i in range(101):
    sum = sum+i
print(sum)


print("\n")
even = 0
odd = 0
for i in range(101):
    if(i%2==0):
        even = even+i
    else:
        odd = odd+i

print(f"Even sum: {even}\nOdd sum: {odd}")