import main
import numpy as np
import array
print("1.sum")
print("2.mean")
print("3.median")
print("4.standard deviation")
print("5.variance")
def __sum():
    return np.sum(main.re)
def __mean():
    return np.mean(main.re)
def __median():
    return np.median(main.re)
def __standarddeviation():
    return np.std(main.re)
def __variance():
    return np.var(main.re)
def main():
    choice=int(input("enter your choice"))
    if choice==1:
        return __sum()
    elif choice==2:
        return __mean()
    elif choice==3:
        return __median()
    elif choice==4:
        return __standarddeviation()
    elif choice==5:
        return __variance()
    else:
        return"exiting"
        
main()