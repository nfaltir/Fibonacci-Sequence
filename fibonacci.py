

# create a dictionary
fibonacci_dictionary = {}  # create dictionary, implement memoization


def fibonacci(n):
    if n in fibonacci_dictionary:
        return fibonacci_dictionary[n]

    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)  # recursive function

    # store value and return it

    fibonacci_dictionary[n] = value
    return value


print("\n==========Fibonacci Sequence==========\n")

# ask user to enter max length of fibonacci sequence
sequence_length = int(
    input("Enter the last (n) number to stop generating a sequence for :"))

for n in range(1, sequence_length + 1):
    print(n, ":", fibonacci(n))
