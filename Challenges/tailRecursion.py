import time

start=time.time_ns()


def tail_recursion(n,acc=1):
    if n==0:
        return acc
    else:
        return n * tail_recursion(n-1,acc)
    

def recursion(n):
    if n==0:
        return 1
    else:
        return n * recursion(n-1)
    
start1=time.time_ns()
print(recursion(5))
end1=time.time_ns()
normal_recursion_run_time=end1-start1
print("Recursion run time: ", normal_recursion_run_time)

start2=time.time_ns()
print(tail_recursion(5))
end2=time.time_ns()

tail_recursion_run_time=end2-start2
print("Tail recursion run time: ", tail_recursion_run_time)

end=time.time_ns()
total_run_time=end-start

print("Percentage faster",(normal_recursion_run_time-tail_recursion_run_time)/total_run_time*100)