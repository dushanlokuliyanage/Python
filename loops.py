countoter = 1
while countoter <= 10:
    print(countoter)
    countoter = countoter + 1

num = [2,3,8,-5,7]
for value in num:
    print(value)

for i in range(1,10):
    print(i)

for num in range(1,100):
    if num ==  5 :
       break
    print(num)

for num in range(1,50):
    if num == 5:
        continue
    print(num)

metrix = [
    [2,5,8],
    [8,1,7],
    [5,4,7]
]

total = 0
 
for row in metrix:
    for element in row:
        total += element
        print(total)