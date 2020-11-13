import numpy as np

import time as tm
import random


def bubble_sort():
    A=np.random.randint(0,100,N)

    t0 = tm.time()
    for j in range(0,len(A)-1):
        for i in range (0, len(A)-j-1):
            if (A[i]>A[i+1]):
                a = A[i]
                A[i]=A[i+1]
                A[i+1] = a
    t1=tm.time()-t0
    print(f'Operation time:{t1}')
    print(A)

    bubble_sort(5000)
