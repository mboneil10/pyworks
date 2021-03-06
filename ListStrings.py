# ***Lists, Strings***

# 1: Write a function that returns the largest element in a list.

def determine_largest_element(elist):
    largest_element = None
    for element in elist:
        if largest_element == None:
            largest_element = element
        elif largest_element < element:
            largest_element = element
    return largest_element

# testing some input
print(str(largest_element([])))
print(str(largest_element([0])))
print(str(largest_element([-1, -2, 4])))
print(str(largest_element([18, 0, 2])))

# 2: Write a function that reverses a list, preferably in place.
def reverse(init_list):
    x = 0
    y = len(init_list)-1
    temp = 0
    while x < y:
        temp = init_list[x]
        init_list[x] = init_list[y]
        init_list[y] = temp
        x = x + 1
        y = y - 1
    return init_list

# testing some input
print(reverse([2,3,5,7]))
print(reverse([3, 5, 8, 7, 20]))

# 3: Write a function that checks whether an element occurs in a list
def contains(list, element):
    contains = False
    for item in list:
        if item == element:
            contains = True
    return contains

# testing some input
print(contains([1, 2, 3], 3))
print(contains([1, 2, 3], 0))
print(contains([2, 2, 7], 2))
print(contains([], 1))

# 4: Write a function that returns the elements on odd positions in a list
def odd_pos(list):
    odds = []
    count = 0
    for item in list:
        if count % 2 == 1:
            odds.append(item)
        count = count + 1
    return odds

print(odd_pos([2, 3, 4, 5]))
print(odd_pos([1]))

# 5: Write a function that computes the running total of a list
def total_sum(list):
    total_sum = 0
    for item in list:
        total_sum = total_sum + item
    return total_sum

print(total_sum([1,2,3,4]))
print(total_sum([-1, 7, 0, 7]))
print(total_sum([1]))

# 6: Write a function that tests whether a string is a palindrome
def palindrome(str):
    palindrome = True
    x = 0
    y = len(str) - 1
    while x < y:
        if str[x] != str[y]:
            palindrome = False
        x = x + 1
        y = y - 1
    return palindrome

# test input
print(palindrome('steta'))
print(palindrome('racecar'))
print(palindrome('a'))

# 7: Write three functions that compute the sum of the numbers in a list: using a for-loop, a while-loop and recursion.
def sum_fl(list):
    sum = 0
    for item in list:
        sum = sum + item
    return sum

def sum_wl(list):
    sum = 0
    length = len(list) - 1
    while length > -1:
        sum = sum + list[length]
        length = length - 1
    return sum

# test input
print(sum_wl([2,4,3,1]))
print(sum_wl([-1, 2, 5]))

def sum_r(list):
    if len(list) - 1 != 0:
        return list[0] + sum_r(list[1:])
    else:
        return list[0]

# test input
print(sum_r([2, 4, 3, 1]))
print(sum_r([0]))
print(sum_r([-1, 2, 5]))

# 8: Write a function `on_all` that applies a function to every element of a list.
# Use it to print the first twenty perfect squares.
def on_all(func, list):
    count = 0
    while count < len(list):
        list[count] = func(list[count])
        count = count + 1
    return list

def perfect_squares(base):
    return base*base

# test input
print(on_all(perfect_squares, [1, 2, 3, 4]))

# 9: Write a function that concatenates two lists.
def concat(list1, list2):
    for item in list2:
        list1.append(item)
    return list1

print(concat(['a', 'b', 'c'], [1, 2, 3]))

# 10: Write a function that combines two lists by alternatingly taking elements
def alt_concat(list1, list2):
    list3 = []
    count = 0
    while count < len(list1):
        list3.append(list1[count])
        if count < len(list2):
            list3.append(list2[count])
        count = count + 1
    return list3

# test input
print(alt_concat(['a', 'b', 'c'], [1, 2, 3]))
print(alt_concat(['a', 'b'], [4]))

# 11: Write a function that merges two sorted lists into a new sorted list.
def sort_and_concat(list1, list2):
    list3 = []
    count = 0
    while count < len(list1):
        if list1[count] < list2[count]:
            list3.append(list1[count])
            list3.append(list2[count])
        else:
            list3.append(list2[count])
            list3.append(list1[count])
        count = count + 1
    return list3

# test input
print(sort_and_concat([1,4,6],[2,3,5]))

# 12: Write a function that rotates a list by k elements. Try solving without creating a copy of the list.
# ex: [1, 2, 3, 4, 5, 6] becomes [3, 4, 5, 6, 1, 2] when k = 2.
def rotate(list, k):
    if k > len(list) - 1:
        k = k % len(list)
    temp = list[:k]
    list = list[k:]
    for item in temp:
        list.append(item)
    return list

# test input
print(rotate([1, 2, 3, 4, 5, 6], 2))
print(rotate([1, 2, 3, 4, 5, 6], 8))

# 13: Write a function that computes the list of the first 100 Fibonacci numbers. First two numbers are 1 and 1.
# The (n+1)th Fib number can be computed by adding the nth and the (n-1)th numbers together.
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

# wasn't able to compute the list of the first 100 Fib numbers because of PyCharm.

# 14: Write a function that takes a number and returns a list of its digits. for 2342 it should return [2, 3, 4, 2]
def digits(number):
    digits = []
    for digit in str(number):
        digits.append(digit)
    return digits

# test the example
print(digits(2342))

# 15: Write functions that add, subtract, and multiply two numbers in their digit-list representation (and return a new digit list)

# Make lists the same length to help with addition, subtraction, and multiplication
def setup(list1, list2):
    missing_indices = 0
    # deal with lists of different lengths
    if len(list1) < len(list2):
        # add zeros to the beginning of list1 so lists are the same length
        missing_indices = len(list2) - len(list1)
        zeros = [0] * missing_indices
        list1 = zeros + list1
    elif len(list1) > len(list2):
        # add zeros to the beginning of list2 so lists are the same length
        missing_indices = len(list1) - len(list2)
        zeros = [0] * missing_indices
        list2 = zeros + list2
    return list1, list2

def add(list1, list2):
    next_digit = 0
    sum = 0
    list1, list2 = setup(list1, list2)
    list3 = [0] * (len(list1))
    index = len(list1) - 1
    while index > -1:
        sum = list1[index] + list2[index]
        if sum > 9:
            list3[index] = sum % 10
            next_digit = (sum - list3[index]) % 9
            list1[index - 1] = list1[index - 1] + next_digit
        else:
            list3[index] = sum
        index = index - 1
    return list3

# test input
print(add([1, 7, 5],[2, 4, 6]))
print(add([1, 0, 0], [2, 0]))

# TODO: fix the neg variable
def sub(list1, list2):
    # this should only instantiate once
    neg = False
    next_digit = 0
    total = 0
    if len(list1) < len(list2):
        # total is negative
        neg = True
        list1, list2 = setup(list2, list1)
    else:
        list1, list2 = setup(list1, list2)
    list3 = [0] * (len(list1))
    index = len(list1) - 1
    while index > -1:
        total = list1[index] - list2[index]
        # produces a negative result, need to go to the left for more digits
        if total < 0:
            # carry the one
            if list1[index - 1] - 1 >= 0:
                list1[index - 1] = list1[index - 1] - 1
                list1[index] = list1[index] + 10
                return sub(list1, list2)
            # total is negative
            neg == True
        list3[index] = total
        index = index - 1
    if neg == False:
        return list3
    else:
        return (-num for num in list3)

# test input
# regular subtraction
# print(sub([2, 2], [1, 0]))
# carry the 1 -- need to expand to the left
# print(sub([1, 0, 0], [2, 0]))
# negative total
print(sub([2, 0], [1, 0, 0]))

def multiply(list1, list2):
    next_digit = 0
    product = 0
    list1, list2 = setup(list1, list2)
    list3 = [0] * (len(list1))
    index = len(list1) - 1
    while index > -1:
        product = list1[index] * list2[index]
        if product > 9:
            # fill in
        else:
            list3[index] = product
        index = index - 1
    return list3

# 16 - 18: Skipped
# 19: Write a function that takes a list of strings and prints them one per line, in a rectangular frame.

def star_frame(list):
    # determine the length by finding the longest string in the list.
    length = longest_string(list)
    width = len(list)
    # append space chars to strings that are smaller than longest string length.
    spaced_list = spacer(list, length)
    frame(length, width, spaced_list)

def longest_string(list):
    index = 0
    longest = 0
    str_length = len(list[index])
    while index < len(list):
        if str_length > longest:
            longest = str_length
        index = index + 1
    return longest

def spacer(list, longest):
    index = 0
    while index < len(list):
        str_length = len(list[index])
        if str_length < longest:
            num_spaces = longest - str_length
            list[index] = list[index] + ' ' * num_spaces
        index = index + 1
    return list

def frame(length, width, list):
    # first line is all stars
    print('*' * (length + 2))
    # lines after and before the last one have a star before and after the string
    for item in list:
        print('*' + str(item) + '*')
    # last string is full of stars
    print('*' * (length + 2))

# test input
star_frame(['bananas', 'orange', 'cherry'])
star_frame(['Hello', 'World', 'this','is', 'a', 'box'])