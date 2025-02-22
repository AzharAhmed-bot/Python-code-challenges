def solution(A):
    max_value=max(A)

    unique_values=set(A)
    range_to_A=set(range(1,max_value+1))
    not_present_values=unique_values-range_to_A

    if len(not_present_values)==0:
        return max_value+1
    else:
        return min(not_present_values)


print(solution([1,2,3,4,5,6,7,8,9]))


