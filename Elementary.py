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

# 8: Write a program that prints all prime numbers
# Skipping this program. Don't want to overload my computer.

# 9: Write a guessing game where the user has to guess a secret number
# After every guess the program tells the user whether their number was too large or too small.
# At the end the number of tries needed should be printed.
# It counts only as one try if they input the same number multiple times consecutively.
secret_number = random.randrange(0, 10)
tries = 0
guesses = []
discovered = False;
guess = input("Please enter a guess for my secret number")

while discovered == False:
    # only counts as one try if they input the same number multiple times
    if int(guess) not in guesses:
        guesses.append(int(guess))
        tries = tries + 1
    if int(guess) > secret_number:
        guess = input("Too large, try again")
    elif int(guess) < secret_number:
        guess = input("Too small, try again")
    else:
        discovered = True
print("You guessed my secret number " + str(secret_number) + "!")
print("Number of tries: " + str(tries))

# 10: Write a program that prints the next 20 leap years
num = 0
leap_year = 2020 # this year is a leap year.
while num < 20:
    num = num + 1
    leap_year = leap_year + 4
    print("leap year " + str(num) + ": " + str(leap_year))

# 11: Write a program that computes the sum of an alternating series where each
# element of the series is an expression of the form
# ((-1)^{k+1})/(2*k-1) for each value of k from 1 to a million, multiplied by 4

k = 1
numerator = 1
denominator = 1
sum = 0

while k < 1000001:
    numerator = (-1)**(k+1)
    denominator = (2*k-1)
    sum = sum + numerator/denominator
    k = k + 1
print(str(4*sum))
