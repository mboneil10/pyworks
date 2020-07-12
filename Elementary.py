import random
# ***Elementary***

# 1: Print "Hello World" to the screen
print("Hello World");

# 2: Ask the user for their name and greets them with their name
user_inp = input("Hello, what is your name?");
print("Greetings " + user_inp);

# 3: Modify the above program such that only users Alice and Bob are greeted with their names
user_inp = input("Hello, what is your name?");
# Remove leading and trailing whitespace, as well as set to lowercase
name = user_inp.strip().lower();
if (name == "alice"):
   print("Greetings Alice");
elif name == "bob":
   print ("Greetings Bob");

# 4: Write a program that asks the user for a number n and prints the sum of the numbers 1 to n
user_inp = input("Please enter a number n to find the sum of numbers 1 to n")
n = int(user_inp)
sum = 0
while n > 0:
    sum = sum + n
    n = n - 1
if sum == 0:
    print("n cannot be less than 1")
else:
    print(sum)

# 5: Modify the previous program such that only multiples of three or five are considered in the sum
user_inp = input("Please enter a number n to find the sum of numbers 1 to n")
n = int(user_inp)
sum = 0
while n > 0:
    if n%3 == 0:
        sum = sum + n
    elif n%5 == 0:
        sum = sum + n
    n = n - 1
print(sum)

# 6: Write a program that asks the user for a number n and gives them the possibility to choose between computing
# the sum and computing the product of 1,...n.
user_num = input("Please enter a number n to submit a list of numbers 1 to n")
n = int(user_num)
user_sym = input("If you would like to find the sum, enter 'sum'. If you would like to find the product, enter 'prod'.")
 # initialize answer as 1 or 0, depending on the symbol
if user_sym == "prod":
   answer = 1
else:
    answer = 0
while n > 0:
    if user_sym == "prod":
        answer = answer * n
    else:
        answer = answer + n
    n = n - 1
print(answer)

# 7: Write a program that prints a multiplication table for numbers up to 12.
nums = range(13)
for x_1 in nums:
    for x_2 in nums:
        product = x_1 * x_2
        print(str(x_1) +"*" + str(x_2) + "=" + str(product))

