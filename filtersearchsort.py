import main
import numpy as np

print("1. Search")
print("2. Sort")
print("3. Filter")


def __search(n):
    return np.where(main.re == n)


def __sort():

    print("1. Ascending")
    print("2. Descending")

    x = int(input("Enter the choice: "))

    if x == 1:
        return np.sort(main.re)

    elif x == 2:
        return np.sort(main.re)[::-1]

    else:
        return "Invalid choice"


def __filter():

    if main.re.ndim == 1:

        start = int(input("Enter the start: "))
        end = int(input("Enter the end: "))

        return main.re[start:end]

    elif main.re.ndim == 2:

        rs = int(input("Enter the starting row: "))
        rend = int(input("Enter the ending row: "))

        cs = int(input("Enter the starting column: "))
        cend = int(input("Enter the ending column: "))

        return main.re[rs:rend, cs:cend]

    elif main.re.ndim == 3:

        ls = int(input("Enter the starting layer: "))
        lend = int(input("Enter the ending layer: "))

        rs = int(input("Enter the starting row: "))
        rend = int(input("Enter the ending row: "))

        cs = int(input("Enter the starting column: "))
        cend = int(input("Enter the ending column: "))

        return main.re[ls:lend, rs:rend, cs:cend]

    else:
        return "Invalid array dimension"


def main():

    while True:

        choice = int(input("Enter your choice: "))

        if choice == 1:

            s = int(input("Enter an element to search: "))
            return __search(s)

        elif choice == 2:

            return __sort()

        elif choice == 3:

            return __filter()

        else:

            return "Exiting"


main()