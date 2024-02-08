"""
Write code that can tell if a number is prime.
A prime number is a number that is only divisible by 1 and itself.
"""
from tkinter import messagebox, simpledialog, Tk

Window = Tk()
Tk().withdraw()

if __name__ == '__main__':
    # TODO)
    #  1. Ask the user for a number
    #  2. Use a for loop, if statement, and modulo to find if the number
    #     is prime.
    #  3. If the number is divisible by any number other than 1 or itself,
    #     the number is not prime.
    pass

num = simpledialog.askinteger(title="", prompt="Choose a number")

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is composite number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")


