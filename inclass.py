import time

# Question 2: Find the sum of numbers from 1 to 10
total_sum = 0

for i in range(1, 11):
    total_sum += i

print("The sum of numbers from 1 to 10 is:", total_sum)

# Question 3: Display the multiplication table of 5
number = 5

print(f"Multiplication Table of {number}:")
for i in range(1, 13):
    print(f"{number} x {i} = {number * i}")

# Question 4: Countdown from a user-entered number
start = int(input("Enter a number to start the countdown: "))

print("Starting countdown...")
while start >= 0:
    print(start)
    time.sleep(1)  # Wait for 1 second
    start -= 1

print("Time's up!")

# Question 5: Input 5 numbers and find their total sum
total = 0

for i in range(1, 6):
    num = float(input(f"Enter number {i}: "))
    total += num

print("The total sum of the 5 numbers is:", total)

# Question 6: Input marks for 10 subjects and calculate average
total_marks = 0
num_subjects = 10

for i in range(1, num_subjects + 1):
    mark = float(input(f"Enter mark for subject {i}: "))
    total_marks += mark

average = total_marks / num_subjects

print(f"\nTotal Marks: {total_marks}")
print(f"Average Mark: {average}")

# Check pass/fail condition
if average >= 75:
    print("Result: Pass")
else:
    print("Result: Fail")


# Question 7: Input 3 numbers using a while loop and find the largest
count = 1
largest = None

while count <= 3:
    num = float(input(f"Enter number {count}: "))

    if largest is None or num > largest:
        largest = num

    count += 1

print("The largest number is:", largest)

#Qoution 8: write a programme the t keeping printing "Hello" until the user enter stop
while True:
    print("Hello")
    user_input = input("Type 'stop' to end or press Enter to continue: ")

    if user_input.lower() == "stop":
        break
