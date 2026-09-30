import main
import array
import numpy as np
print("combine and split array")
print("1.combine")
print("2.split")
print("3.go back to main menu")

def __combine(n):
    print("1. Vertical stack")
    print("2. Horizontal stack")

    c = int(input("Enter your choice: "))

    n = np.array(list(map(int, n.split())))

    if c == 1:                      # vstack
        if main.re.ndim == 1:
            if n.size != main.re.size:
                return "Number of elements must be same"
            n = n.reshape(1, -1)

        elif main.re.ndim == 2:
            n = n.reshape(-1, main.re.shape[1])

        elif main.re.ndim == 3:
            n = n.reshape(-1, main.re.shape[1], main.re.shape[2])

        return np.vstack((main.re, n))

    elif c == 2:                    # hstack
        if main.re.ndim == 1:
            return np.hstack((main.re, n))

        elif main.re.ndim == 2:
            n = n.reshape(main.re.shape[0], -1)

        elif main.re.ndim == 3:
            n = n.reshape(main.re.shape[0], -1, main.re.shape[2])

        return np.hstack((main.re, n))

    else:
        return "Exiting"
        exit()
def __split(n):

    print("1. Split")
    print("2. Vertical split")
    print("3. Horizontal split")

    d = int(input("Enter your choice: "))

    # =========================
    # 1D ARRAY
    # =========================
    if main.re.ndim == 1:

        if d == 1:

            if main.re.size % n == 0:
                return np.split(main.re, n)
            else:
                return "Invalid number of splits"

        elif d == 2:
            return "Vertical split is not applicable to 1D array"

        elif d == 3:
            return "Horizontal split is not applicable to 1D array"

        else:
            return "Invalid choice"

    # =========================
    # 2D ARRAY
    # =========================
    elif main.re.ndim == 2:

        if d == 1:

            if main.re.size % n == 0:
                return np.split(main.re, n)
            else:
                return "Invalid number of splits"

        elif d == 2:

            if main.re.shape[0] % n == 0:
                return np.vsplit(main.re, n)
            else:
                return "Invalid number of splits"

        elif d == 3:

            if main.re.shape[1] % n == 0:
                return np.hsplit(main.re, n)
            else:
                return "Invalid number of splits"

        else:
            return "Invalid choice"

    # =========================
    # 3D ARRAY
    # =========================
    elif main.re.ndim == 3:

        if d == 1:

            axis = int(input("Enter axis (0, 1, or 2): "))

            if axis not in [0, 1, 2]:
                return "Invalid axis"

            if main.re.shape[axis] % n == 0:
                return np.split(main.re, n, axis=axis)
            else:
                return "Invalid number of splits"

        elif d == 2:

            if main.re.shape[0] % n == 0:
                return np.vsplit(main.re, n)
            else:
                return "Invalid number of splits"

        elif d == 3:

            if main.re.shape[1] % n == 0:
                return np.hsplit(main.re, n)
            else:
                return "Invalid number of splits"

        else:
            return "Invalid choice"

    else:
        return "Invalid array dimension"

def main():
   while True:
      e=int(input("enter your  choice"))
      

      if e==1:
         com=input("enter the no of elements seperated by spaces")
         return __combine(com)
      elif e==2:
         n=int(input("enter the no of split parts of array you want"))
         return __split(n)

      else:
         return"exiting "
         
main()
         
