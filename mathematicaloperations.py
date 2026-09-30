import numpy as np
import main

print("Select your choice")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Going back to main menu")


def __addition(n):
    try:
        n = list(map(int, n.split()))

        if len(n) == np.size(main.re):
            np1 = np.array(n).reshape(main.re.shape)
            return np1 + main.re
        else:
            print("Your number of elements is not equal to the number of elements in the original array")

    except Exception as e:
        print("Your error is:", e)


def __subtraction(n):
    try:
        n = list(map(int, n.split()))

        if len(n) == np.size(main.re):
            np1 = np.array(n).reshape(main.re.shape)
            return np1 - main.re
        else:
            print("Your number of elements is not equal to the number of elements in the original array")

    except Exception as e:
        print("Your error is:", e)


def __multiplication(n):
    try:
        n = list(map(int, n.split()))

        if len(n) == np.size(main.re):
            np1 = np.array(n).reshape(main.re.shape)
            return np1 * main.re
        else:
            print("Your number of elements is not equal to the number of elements in the original array")

    except Exception as e:
        print("Your error is:", e)


def __division(n):
    try:
        n = list(map(int, n.split()))

        if len(n) == np.size(main.re):
            np1 = np.array(n).reshape(main.re.shape)
            return np1 / main.re
        else:
            print("Your number of elements is not equal to the number of elements in the original array")

    except Exception as e:
        print("Your error is:", e)


def main():
    e = int(input("Enter your choice: "))

    match e:
        case 1:
            noof = input("Enter elements for addition: ")
            return __addition(noof)

        case 2:
            noof = input("Enter elements for subtraction: ")
            return __subtraction(noof)

        case 3:
            noof = input("Enter elements for multiplication: ")
            return __multiplication(noof)

        case 4:
            noof = input("Enter elements for division: ")
            return __division(noof)

        case 5:
            return"Exiting towards main menu"
            exit()

        case _:
            return"Invalid choice"


main()
