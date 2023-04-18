# Q-8 Write a Python script to input two numbers and find their sum.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

sum = num1 + num2

print("The sum of", num1, "and", num2, "is", sum)


# Q-9 Write a Python script to input side of a square and display its area.

side = int(input("Enter the length of a side of the square: "))

area = side*side

print("The area of the square with side ", side, "is ", area)

#Q-10 Write a Python script to input length and breadth of a rectangle and display its area and perimeter.

length = int(input("Enter the length of the rectangle: "))
breadth = int(input("Enter the breadth of the rectangle: "))

area = length * breadth
perimeter = 2 * (length + breadth)

print("The area of the rectangle with length", length, "and breadth", breadth, "is", area)
print("The perimeter of the rectangle with length", length, "and breadth", breadth, "is", perimeter)

# Q-11 Write a Python script to input an integer and display its square and cube.

num = int(input("Enter an integer: "))

square = num ** 2
cube = num ** 3

print("The square of", num, "is", square)
print("The cube of", num, "is", cube)

# Q-12 Write a Python script to swap two numbers.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("Original numbers: num1 = ", num1, "and num2 = ", num2)

num3 = num1
num1 = num2
num2 = num3

print("Swapped numbers: num1 = ", num1, "and num2 = ", num2)

# Q- 13 Write a Python script to input a number and print its preceding and succeeding number.

num = int(input("Enter a number: "))

preceding_num = num - 1
succeeding_num = num + 1

print("The preceding number is: ", preceding_num)
print("The succeeding number is: ", succeeding_num)

#Q-14 Write a Python script to input cost price and selling price of an item display profit/loss.

cost_price = float(input("Enter the cost price: "))
selling_price = float(input("Enter the selling price: "))

profit_loss = selling_price - cost_price

if profit_loss > 0:
    print("There is a profit of", profit_loss)
elif profit_loss < 0:
    print("There is a loss of", abs(profit_loss))
else:
    print("There is no profit or loss.")

#Q-15 Write a Python script to input a number and print its first five multiples.

num = int(input("Enter a number: "))

print("The first five multiples of", num, "are:")
for i in range(1, 6):
    print(num * i)

# Q-16 Write a Python script to input name, class, section and subject and display all information in the format of name tag.

name = input("Enter your name: ")
class_name = input("Enter your class: ")
section = input("Enter your section: ")
subject = input("Enter your subject: ")

print("Hello, my name is", name)
print("I am studying in class", class_name, "and section", section)
print("My favorite subject is", subject)



