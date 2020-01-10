This program will asks the user how many Fibonnaci numbers to generate and then generates them. 


Definition

Fibonacci sequence: The Fibonacci sequence is a set of numbers that starts with a one or a zero, followed by a one, and proceeds based on the rule that each number (called a Fibonacci number) is equal to the sum of the preceding two numbers. If the Fibonacci sequence is denoted F (n), where n is the first term in the sequence, the following equation obtains for n = 0, where the first two terms are defined as 0 and 1 by convention. (https://whatis.techtarget.com/definition/Fibonacci-sequence)


Example:

Fibonnacci Sequence first set = [1,1,2,3,5,8,13,21]


Input
1. Ask user how many numbers to generate

Output
1. program will generate fibonacci sequence.

---------------------------------------------------Without a dictionary-------------------------------------------

# this function will retun the nth term


 def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
 funtion will retun the sum of the previous two terms
        return fibonacci(n-1) + fibonacci(n-2)

 for n in range(1, 10001):
 print(n, "=", fibonacci(n)) #it stops running when n = 41th (very slow)

 solution, speed program by using memoization by using a dictionary

---------------------------------------------------With a dictionary-----------------------------------------------

fibonacci_dictionary = {}


def fibonacci(n):
    if n in fibonacci_dictionary:
        return fibonacci_dictionary[n]

    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)

    # store value and return it

    fibonacci_dictionary[n] = value
    return value

# run test again


for n in range(1, 200):
    print(n, ":", fibonacci(n))