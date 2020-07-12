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
