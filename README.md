NumPy Analyzer

Author: Shrey Shah

📌 Project Description

NumPy Analyzer is a Python-based menu-driven project designed to perform different operations on NumPy arrays.

The project is divided into multiple Python modules, with each module responsible for a specific category of array operations.

It supports 1D, 2D, and 3D NumPy arrays.

🚀 Features

The project provides the following features:

Create NumPy Arrays

Create 1D arrays

Create 2D arrays

Create 3D arrays

Perform indexing

Perform slicing

Mathematical Operations

Addition

Subtraction

Multiplication

Division

Combine and Split Arrays

Vertical stacking using vstack()

Horizontal stacking using hstack()

Splitting using split()

Vertical splitting using vsplit()

Horizontal splitting using hsplit()

Supports 1D, 2D, and 3D arrays

Search, Sort and Filter

Search values using np.where()

Sort in ascending order

Sort in descending order

Filter arrays using indexing and slicing

Aggregates and Statistics

Sum

Mean

Median

Standard deviation

Variance

Exit

Exit the program safely from the main menu

📂 Project Structure
NumPy-Analyzer/
│
├── main.py
├── arraycreation.py
├── mathematicaloperations.py
├── combinesplit.py
├── filtersearchsort.py
├── aggregationfunction.py
└── README.md

📄 File Description
1. main.py

This is the main menu of the project.

It allows the user to select between:

1. Create a NumPy array
2. Perform mathematical functions
3. Combine or split arrays
4. Search, sort and filter arrays
5. Compute aggregates and statistics
6. Exit


It also manages the current NumPy array and passes it to the required modules.

2. arraycreation.py

This module is responsible for creating NumPy arrays.

It supports:

1D arrays

2D arrays

3D arrays

It also provides:

Indexing

Slicing

Example 3D shape:

(layers, rows, columns)

3. mathematicaloperations.py

This module performs element-wise mathematical operations.

Supported operations:

Addition
Subtraction
Multiplication
Division


The new array is reshaped to match the shape of the existing array before performing the operation.

For example:

array1 + array2

4. combinesplit.py

This module handles combining and splitting NumPy arrays.

Combining

It supports:

np.vstack()
np.hstack()

Splitting

It supports:

np.split()
np.vsplit()
np.hsplit()


For 3D arrays, np.split() can use:

axis = 0
axis = 1
axis = 2


The program checks whether the selected dimension can be divided equally before splitting.

5. filtersearchsort.py

This module provides three operations.

Search

Uses:

np.where()


to find the position of a specified value.

Sort

Ascending:

np.sort(array)


Descending:

np.sort(array)[::-1]

Filter

Filtering is performed using NumPy indexing and slicing.

For example, a 2D array can be filtered using:

array[row_start:row_end, column_start:column_end]


A 3D array can be filtered using:

array[layer_start:layer_end,
      row_start:row_end,
      column_start:column_end]

6. aggregationfunction.py

This module performs statistical calculations using NumPy.

Available functions:

np.sum()
np.mean()
np.median()
np.std()
np.var()

Operation	NumPy Function
Sum	np.sum()
Mean	np.mean()
Median	np.median()
Standard Deviation	np.std()
Variance	np.var()
🧮 NumPy Concepts Used

This project demonstrates several important NumPy concepts:

np.array()

ndim

shape

size

reshape()

Indexing

Slicing

np.where()

np.sort()

np.vstack()

np.hstack()

np.split()

np.vsplit()

np.hsplit()

np.sum()

np.mean()

np.median()

np.std()

np.var()

📐 Array Dimensions

The project works with three types of arrays.

1D Array
[10 20 30 40]


Shape:

(4,)

2D Array
[[10 20]
 [30 40]]


Shape:

(2, 2)

3D Array
[
    [[1 2]
     [3 4]]

    [[5 6]
     [7 8]]
]


Shape:

(2, 2, 2)

🔢 Important Splitting Rules

For a 2D array:

split      → based on total elements/selected axis
vsplit     → based on rows
hsplit     → based on columns


For a 3D array:

axis 0 → layers
axis 1 → rows
axis 2 → columns


For equal splitting, the selected dimension must be divisible by the number of requested parts.

For example:

Shape = (6, 4, 8)
Number of splits = 2


All three axes can be divided by 2.

🛠️ Requirements

You need:

Python 3.x

NumPy

Install NumPy using:

pip install numpy

▶️ How to Run

Place all six Python files in the same directory.

Then run:

python main.py


The program will display the main menu.

Example:

Numpy Analyzer
Please choose your choice

1. Create a numpy array
2. Perform mathematical function
3. Combine or split array
4. Search, sort, filter array
5. Compute aggregates and statistics
6. Exit

Enter your choice:


Select the required option and follow the instructions displayed by the program.

⚠️ Input Requirements

Enter numeric values when the program asks for array elements.

For 2D arrays, provide the correct number of elements according to rows × columns.

For 3D arrays, provide the correct number of elements according to layers × rows × columns.

When splitting an array, the selected dimension should be divisible by the number of requested parts.

Avoid division by zero during division operations.

🎯 Purpose of the Project

The purpose of NumPy Analyzer is to practice and demonstrate:

Python functions

Python modules

Menu-driven programming

NumPy arrays

Array dimensions and shapes

Array indexing and slicing

Array manipulation

Mathematical operations

Searching and sorting

Statistical operations

👨‍💻 Author

Shrey Shah

📜 License

This project is created for educational and learning purposes.
