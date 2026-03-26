# num1 = float(input("Enter Salry: "))
# intsrest = float(input("Enter Intesrest: "))
# years = float(input("How many years "))

# result = num1 * intsrest / 100
# final  = result * years

# print("Result: ", final)


list = [10,20,30,40,50]

# print(max(list))
# print(min(list))

# num1 = input("Enter First number:" )
# num2 = input("Enter second number:" )

# if num1 > num2:
#     print("Larges Is: ", num1)
# else:
#       print("Largest Is: ", num2)

# write a program to check a person aligle age 

while True:
    # Age = int(input("Enter Your Age: "))
    # if Age >= 18:
    #     print("Eligeble to Vote")
    # else:
    #     print("Not Aligble")

        #Finding max of three num
    num1 = input("Enter First number: " )
    num2 = input("Enter second number: " )
    num3 = input("Enter third number: " )

    if num1 > num2:
        print("Larges Is: ", num1)
    elif num1 > num3:
        print("Largest Is: ", num1)
    elif num3 > num2:
        print("Largest Is: ", num3)
    elif num3 > num1:
        print("Largest Is: ", num3)
    elif num2 > num3:
        print("Largest is: ", num2)
 

 # When student enter the marks then print the grade of the student

    marks = int(input("Enter Your Marks: "))
    if marks >= 75:
        print("Grade A")
    elif marks >= 65:
        print("Grade B")
    elif marks >= 55:
        print("Grade C")
    elif marks >= 40:
        print("Grade Fass")
    else:
        print("Fail")

        match marks:
            case 75:
                print("Grade A")
            case 65:
                print("Grade B")
            case 55:
                print("Grade C")
            case 40:
                print("Grade D")
            case _:
                print("Fail")

#Write down how to cal ur electricity bill 0-50 per uni 10 and 50 - 90 per unit 15 and more than  90 per unit 50 and gov tax 1000

    unit = int(input("Enter Your Unit: "))
    if unit <= 30:
        bill = unit * 5 + 1000
        print("Your Bill is: ", bill)   
    elif unit <= 60:
        bill = unit * 10 + 1000
        print("Your Bill is: ", bill)  
    elif unit <= 100:
        bill = unit * 15 + 1000
        print("Your Bill is: ", bill)   
    else:
        bill = unit * 50 + 1000
        print("Your Bill is: ", bill)   



            
       