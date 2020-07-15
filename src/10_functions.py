# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

def is_even(n):
    if n % 2 == 0:
        print(True)
        return True
    else:
        print(False)
        return False

is_even(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

def is_even_print(n):
    if n % 2 == 0:
        print("Even Number!")
    else:
        print("Odd Number!")

is_even_print(num)

# YOUR CODE HERE

