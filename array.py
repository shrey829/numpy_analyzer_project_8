import numpy as np

print("Your choice is array")
print("Enter your choice for type of array")
print("1. 1D array")
print("2. 2D array")
print("3. 3D array")


def __one_d(s):
    s = list(map(int, s.split()))

    oned = np.array(s)

    print("Enter your operation")
    print("1. Indexing")
    print("2. Slicing")
    print("3. Return back")

    w = int(input("Enter your choice: "))

    if w == 2:
        c = int(input("Enter your start: "))
        t = int(input("Enter your end: "))
        g = int(input("Enter your step: "))

        return oned, oned[c:t:g]

    elif w == 1:
        index = int(input("Enter the index to be found: "))

        return oned, oned[index]

    elif w == 3:
        return "Exiting the operations"


def __two_d(a, b, c):
    e = list(map(int, c.split()))

    twod = np.array(e).reshape(a, b)

    print("Enter your operation")
    print("1. Indexing")
    print("2. Slicing")
    print("3. Return back")

    w = int(input("Enter your choice: "))

    if w == 2:
        print("Enter your row range")

        u = int(input("Enter row start: "))
        t = int(input("Enter row end: "))

        print("Enter your column range")

        g = int(input("Enter column start: "))
        f = int(input("Enter column end: "))

        return twod, twod[u:t, g:f]

    elif w == 1:
        print("Enter the index of row and column")

        s = int(input("Enter row: "))
        r = int(input("Enter column: "))

        return twod, twod[s, r]

    elif w == 3:
        return "Exiting the operations"


def __three_d(d, e, f, g):
    y = list(map(int, g.split()))

    threed = np.array(y).reshape(d, e, f)

    print("Enter your operation")
    print("1. Indexing")
    print("2. Slicing")
    print("3. Return back")

    w = int(input("Enter your choice: "))

    if w == 1:
        print("Enter your layer, row and column")

        a = int(input("Enter your layer: "))
        b = int(input("Enter your row: "))
        c = int(input("Enter your column: "))

        return threed, threed[a, b, c]

    elif w == 2:
        print("Enter your layer range")

        a = int(input("Enter layer start: "))
        b = int(input("Enter layer end: "))

        print("Enter your row range")

        c = int(input("Enter row start: "))
        k = int(input("Enter row end: "))

        print("Enter your column range")

        j = int(input("Enter column start: "))
        l = int(input("Enter column end: "))

        return threed, threed[a:b, c:k, j:l]

    elif w == 3:
        return "Exiting the operations"


def main():

    while True:
        print("\n----------------------")
        print("1. 1D array")
        print("2. 2D array")
        print("3. 3D array")
        print("4. Exit")
        print("----------------------")

        c = int(input("Enter your choice: "))

        if c == 1:

            noelements = input(
                "Enter the elements separated by spaces: "
            )

            result = __one_d(noelements)
            print(result)

        elif c == 2:

            rows = int(input("Enter number of rows: "))
            col = int(input("Enter number of columns: "))

            ele = input(
                "Enter the elements separated by spaces: "
            )

            result = __two_d(rows, col, ele)
            print(result)

        elif c == 3:

            lay = int(input("Enter number of layers: "))
            r = int(input("Enter number of rows: "))
            c = int(input("Enter number of columns: "))

            q = input(
                "Enter the elements separated by spaces: "
            )

            result = __three_d(lay, r, c, q)
            print(result)

        elif c == 4:
            print("Exiting program...")
            break

        else:
            print("Invalid choice")


main()