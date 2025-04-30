import math
import time

class PrimeFactorizer:
    def __init__(self,number):
        self.number=number
    
    @property
    def factor(self):
        num=self.number
        result={}
        sqrt=int(math.sqrt(num))
        for i in range(2,sqrt+1):
            # print(i)
            while num % i ==0:
                num= num / i
                result[i]=result.get(i,0)+1
        
        if num > 1:
            result[num]=result.get(num,0)+1
        return result

    
    @property
    def poorFactor(self):
        
        num=self.number
        result={}
        for i in range(2,num+1):
            # print(i)
            while num % i ==0:
                num= num / i
                result[i]=result.get(i,0)+1
        
        if num > 1:
            result[num]=result.get(num,0)+1
        return result

start_time = time.thread_time_ns()               
print(PrimeFactorizer(245).factor)
end_time = time.thread_time_ns()

print("Efficient factorization: ",end_time-start_time)

start_time_2 = time.thread_time_ns()               
print(PrimeFactorizer(245).poorFactor)
end_time_2 = time.thread_time_ns()

print("Poor factorization: ",end_time_2-start_time_2)

