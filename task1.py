import numpy as np
 # TEMP:
def bubble_sort(A):
    A=np.array([4,3,2,1])

    for j in range(0,len(A)-1):
        for i in range (0, len(A)-j-1):
            if (A[i]>A[i+1]):
                a = A[i]
                A[i]=A[i+1]
                A[i+1] = a
            print(A)
