'''
Ceiling in a sorted array
Last Updated : 10 Feb, 2023
Given a sorted array and a value x, the ceiling of x is the smallest element in an array greater than or equal to x, and the floor is the greatest element smaller than or equal to x. Assume that the array is sorted in non-decreasing order. Write efficient functions to find the floor and ceiling of x. 
Examples : 

For example, let the input array be {1, 2, 8, 10, 10, 12, 19}
For x = 0:    floor doesn't exist in array,  ceil  = 1
For x = 1:    floor  = 1,  ceil  = 1
For x = 5:    floor  = 2,  ceil  = 8
For x = 20:   floor  = 19,  ceil doesn't exist in array
'''
def solutionForFindingCeiling(arr, x):
    n = len(arr)
    if x < arr[0]:
        return arr[0]
    if x > arr[n-1]:
        return -1
    for i in range(n):
        if arr[i] >= x:
            return arr[i]
    return -1

def solutionForFindingFloor(arr, x):
    n = len(arr)
    if x < arr[0]:
        return -1
    if x > arr[n-1]:
        return arr[n-1]
    for i in range(n):
        if arr[i] > x:
            return arr[i-1]
    return -1