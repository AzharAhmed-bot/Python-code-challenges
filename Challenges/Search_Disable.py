def check_prime(num):
    num=int(num)
    if num < 2:
        return False
    
    for i in range(2,int(num**0.5)+1):
        if num % i ==0:
            return False
    return True

print(check_prime(5))


def search_disable(log):
    logs=log.split()
    result=dict()
    for l in logs:
        if len(l)!=4 or not check_prime(l) or (l[2] not in ['2','3']):
            continue
        else:
            if l not in result:
                result[l]=1
            else:
                result[l]+=1
    
    total=sum(count for count in result.values() if count>3)
    print(total)
    return "match disable bot" if total > 50 else "no match continue"
        


log= '2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031'

print(search_disable(log))


def quicksort(array):
    if len(array) < 2:
        return array
    n=len(array)
    pivot=array[n//2]
    left=[num for num in array if num < pivot]
    middle=[num for num in array if num == pivot]
    right=[num for num in array if num > pivot]

    return quicksort(left) + middle + quicksort(right)

print(quicksort([3,5,9,12,4,8,2]))