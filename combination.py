# Example of input -> {"3XX": 11, "1CX": 12, "6XX": 15, "5XX": 16} -> Position 0 is front of the line
# Function returns array with all possinle combinatins

def array_combination():
    # importing Numpy package
    import numpy as np

    # creating 2 numpy arrays
    array_1 = np.array([1, 2])
    array_2 = np.array([4, 6])

    print("Array-1")
    print(array_1)

    print("\nArray-2")
    print(array_2)

    # combination of elements of array_1 and array_2
    # using numpy.meshgrid().T.reshape()
    comb_array = np.array(np.meshgrid(array_1, array_2)).T.reshape(-1, 2)

    print("\nCombine array:")
    print(comb_array)

array_combination()