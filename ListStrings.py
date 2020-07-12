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
