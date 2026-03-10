firsttFile = open("hello.txt") # one
open("hello.txt","r") # "r" means read mood

reading = firsttFile.read()
print(reading)

reading = firsttFile.readline()
print(reading)

with open("hello.txt", "r") as firstFile:
    reading = firstFile.read()
    print(reading)