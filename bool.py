# a = 200
# b = 400

# if a > b:
#     print("A is grater than B")
# else:
#     print("B is not greter than A")

# while True:
#     age = int(input("How old are you : "))
#     if age > 18:
#         print("Go Ahead")
#     else:
#         print("Please Exit")
#     userAccess = input("If you wanna countinu? (y/n)")
#     if userAccess == "n":
#         print("Thank you")
#         break

age = 52

message = "Aligible" if age >= 18 else "Not aligible"
print(message)

#Age is between 18 and 75

age = 25
if 18 <= age > 75:
    print("Eligible")

# Interble 
for x  in "Python":
    print(x)


    command  = ""
    while command != "qouit":
       command = input(">")
       print("ECHO" ,command)