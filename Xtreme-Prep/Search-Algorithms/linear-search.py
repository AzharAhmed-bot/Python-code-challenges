def linearSearch(array, target):
    for num in array:
        if num == target:
            return True
    return False


print(linearSearch([1, 2, 3, 4, 5], 3))  






# Problem 1 : Indexes of Subarray Sum
def IndexesOfSubarraySum(arr,target):
    sum = 0
    start = 0

    for end in range(len(arr)):
        sum+= arr[end]

        while sum > target and start <=end:
            sum -=arr[start]
            start+=1
        
        if sum == target:
            return [start+1,end+1]
    
    return [-1]


print(IndexesOfSubarraySum([5, 3, 4], 2))


# Problem 2: Missing in array
def MissingInArray(arr):
    n = len(arr)+1
    total = n * (n+1) // 2
    return total - sum(arr)

print(MissingInArray([1, 2, 3, 5]))

    
# Problem 3: 2nd largest in array
def secondLargestInArray(arr):
    if len(arr) < 2:
        return -1
    
    first =-1
    second = -1
    for num in arr:
        if num > first:
            second = first
            first = num
        # Cases of duplicates eg [5,5,5]
        elif num > second and num != first:
            second = num
    
    return second
    
        

print(secondLargestInArray([1, 2, 3, 5]))




# 4: Majority Element
def MajorityElement(arr):
    memory={}

    for num in arr:
        memory[num] = memory.get(num,0) + 1
    
    for key in memory:
        if memory[key] > len(arr) // 2:
            return key
    
    return -1


print(MajorityElement([1, 1, 2, 1, 3, 5, 1]))



# 5: Kth smallest
def kthSmallest(arr,k):
    arr.sort()
    return arr[k-1]

print(kthSmallest([1, 2, 3, 4, 5], 3))


# 6: Binary Search
def binarySearch(array, target):
    leftmost = 0
    rightmost = len(array)-1

    while leftmost <= rightmost:
        midpoint = (leftmost + rightmost) // 2

        if array[midpoint] == target:
            return midpoint
        elif array[midpoint] < target:
            leftmost = midpoint + 1
        else:
            rightmost = midpoint-1
    
    return -1


def peakElement(arr):
    n =  len(arr)
    if len(arr) == 1:
        return True
    
    if arr[0] > arr[1] or arr[n-1] > arr[n-2]:
        return True
    for i in range(1, n-1):
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            return True
    
    return False
       
print(peakElement([1, 2, 4, 5, 7, 8, 3]))

def findFloor(arr,x):
    result = 0

    for i  in range(len(arr)):
        if arr[i] <=x:
            result = i
    
    return result

print(findFloor([1, 2, 8, 10, 10, 12, 19], 0))


from collections import Counter

def isSubset(a,b):
    count_a = Counter(a)
    count_b = Counter(b)

    for item,freq in count_b.items():
        if count_a[item] < freq:
            return False
    return True


print(isSubset([11, 7, 1, 13, 21, 3, 7, 3],[11, 3, 7, 1, 7]))

def commonElemets(arr1, arr2, arr3):
    return list(sorted(set(arr1) & set(arr2) & set(arr3))) if len(set(arr1) & set(arr2) & set(arr3)) > 0 else [-1]

print(commonElemets([11, 13, 14, 45, 62, 72, 79, 90], [13, 24, 27, 31, 62, 74, 89, 89, 96], [12, 48, 58, 60, 62, 65, 88]))