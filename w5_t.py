import numpy as np
import matplotlib.pyplot as plt
import time

# Set up a random list of integers
n = 1000
rng = np.random.default_rng()
my_list = rng.integers(1, n+1, size=n)

def bubble_sort(arr):
    '''
    Sorts the list or array arr using bubble sort.
    Input: arr (list or array): the array to sort
    Output: sorted_arr (list): a copy of arr, with elements sorted in order
    '''
    # Make a copy first
    sorted_arr = arr.copy()
    counter = 1

    # Keep looping over the list until there are no more swaps
    while True:
        # Keep track of whether we've swapped anything this time
        swapped = False

        # Compare each consecutive pair of elements
        for i in range(len(sorted_arr)-counter):
            if sorted_arr[i] > sorted_arr[i+1]:
                # Swap!
                sorted_arr[i], sorted_arr[i+1] = sorted_arr[i+1], sorted_arr[i]
                swapped = True

        # The next largest element is now at the correct place, we don't need to check it anymore
        counter += 1

        # If at this point swapped is still False, we can finish
        if not swapped:
            return sorted_arr

my_list_bubble = bubble_sort(my_list)
my_list_sorted = sorted(my_list)
print(my_list_bubble)
print(my_list_sorted)
print(np.all(my_list_bubble == my_list_sorted))
'''
sorted(): 基础的序列升序排序
ref:
https://www.cnblogs.com/yushuo1990/p/5880041.html
'''
