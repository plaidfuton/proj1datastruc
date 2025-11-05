#Name: Ryan Nielson
#ID: 86219673
#Email: rnielson@unomaha.edu

import math
import time
import random
import sys

##########################################################
# You are not allowed to add additional functions.
# You must keep the structure of the code below.
# That is, you only need to implement (revise) the given pseudo code in Python.

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                swap(arr, j, j+1)

def selectionSort(arr):
    n = len(arr)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        swap(arr, i, min_idx)

def insertionSort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i-1

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def shellSort(arr):
    n = len(arr)
    gap = math.floor(n/2)

    while (gap >= 1):
        for i in range(gap, n):
            j = i
            while j >= gap and arr[j] < arr[j - gap]:
                swap(arr, j, j-gap)
                j -= gap
        gap = math.floor(gap/2)

def merge(arr, temp, LEFT, CENTER, RIGHT):
    leftIdx = LEFT
    rightIdx = CENTER + 1
    merge_start = LEFT

    while leftIdx <= CENTER and rightIdx <= RIGHT:
        if arr[leftIdx] <= arr[rightIdx]:
            temp[merge_start] = arr[leftIdx]
            leftIdx += 1
        else:
            temp[merge_start] = arr[rightIdx]
            rightIdx += 1

        merge_start += 1

    while leftIdx <= CENTER:
        temp[merge_start] = arr[leftIdx]
        leftIdx += 1
        merge_start += 1

    while rightIdx <= RIGHT:
        temp[merge_start] = arr[rightIdx]
        rightIdx += 1
        merge_start += 1

    for i in range(LEFT, RIGHT+1):
        arr[i] = temp[i]

def mergeSort(arr, temp, left, right):
    if left >= right:
        return

    center = math.floor((left + right)/2)

    mergeSort(arr, temp, left, center)
    mergeSort(arr, temp, center+1, right)

    merge(arr, temp, left, center, right)

def quickSort(arr, LEFT, RIGHT):
    if LEFT < RIGHT:
        mid = math.floor((LEFT + RIGHT) / 2)
        pivot = arr[mid]

        leftIdx = LEFT
        rightIdx = RIGHT

        while leftIdx <= rightIdx:
            while arr[leftIdx] < pivot:
                leftIdx += 1
                
            while arr[rightIdx] > pivot:
                rightIdx -= 1

            if leftIdx <= rightIdx:
                swap(arr, leftIdx, rightIdx)
                leftIdx += 1
                rightIdx -= 1

        quickSort(arr, LEFT, leftIdx-1)
        quickSort(arr, leftIdx, RIGHT)

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def printArray(arr):
    n = len(arr)

    for i in range(0,  n):
        print(str(arr[i]) + ' ', end=' ')

    print('\n')

def generateRandomNumbers(cnt, type):
    # This function will generate Integer array of which size is cnt.
    # The range of the generated numbers is 0 ~ cnt
    # type 1: totally random numbers, 2: sorted_numbers, 3: reverse-order_numbers, else: not supported
    intList = []

    if type == '1':
       for i in range(int(cnt)):
           intList.append((random.randint(0, int(cnt))))
    elif type == '2':
        for i in range(int(cnt)):
            intList.append(i)
    elif type == '3':
        for i in range((int(cnt)-1), -1, -1):   #must be int(cnt)-1, -1, -1 for 0-98 in a 99 element list
            intList.append(i)

    return intList


if __name__ == '__main__':
    # The parameters from the execution will be used as prameters for the generateRandomNumbers function below.
    # You must receive parameters from the command lines like below.
    # > python3 SortingArray.py 3 1000000 6 (create reverse-order numbers (0-1000000 and sort it using QuickSort)

    if (len(sys.argv) == 4                                      # Exception Handling, checking for exactly 3 commandline arguments ('SortingArray.py' is sys.argv[0]),
            and sys.argv[3] in ['1', '2', '3', '4', '5', '6']   # number entered for sorting method is 1 through 6
            and int(sys.argv[2]) > -1                           # total number of elements of the list must be greater than or equal to 0
            and sys.argv[1] in ['1', '2', '3']):                # style of array generated must be '1': random | '2': sorted | '3': reversed
        arr = generateRandomNumbers(sys.argv[2], sys.argv[1])

        if len(arr) < 100:
            print('Before sort: ')
            printArray(arr)

        start_time = time.time() # Timer Start

        # Sorting method will be provided as the second parameter for main args[2]

        if sys.argv[3] == '1':
            bubbleSort(arr) # 1: Bubble Sort
        elif sys.argv[3] == '2':
            selectionSort(arr) # 2: Selection Sort
        elif sys.argv[3] == '3':
            insertionSort(arr) # 3: Insertion Sort
        elif sys.argv[3] == '4':
            shellSort(arr) # 4: Shell Sort
        elif sys.argv[3] == '5':
            mergeSort(arr, [0]*len(arr), 0, (len(arr)-1)) # 5: Merge Sort
        elif sys.argv[3] == '6':
            quickSort(arr, 0, (len(arr)-1)) # 6: Quick Sort

        end_time = time.time() # Timer end
        elapsed_time = end_time - start_time
        print(f"Elapsed sorting time: {elapsed_time:.4f} seconds") # Print elapsed time for sorting

        # Print only when cnt is less than 100
        if len(arr) < 100:
            print('After sort: ')
            printArray(arr)

    else:
        print("Please enter valid command line arguments. Usage: 'SortingArray.py [1-3] [>=0] [1-6]'")          # Exception failure statement