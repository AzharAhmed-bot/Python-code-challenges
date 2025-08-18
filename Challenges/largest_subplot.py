def gcd(a,b):
    if b==0:
        return a
    
    return gcd(b,a%b)

print(gcd(1680,640))

def prime_factors(num):
    factors = {}
    length = int(num**0.5) + 1
    for i in range(2,length):
        while num%i==0:
            factors[i] = factors.get(i,0) + 1
            num = num//i
    if num>1:  
        factors[num]=factors.get(num,0) + 1
    return factors



def lcm(a,b):
    prime_factors_a = prime_factors(a)
    prime_factors_b = prime_factors(b)
    result={}
    
    all_primes=set(prime_factors_a) | set(prime_factors_b)
    for prime in all_primes:
        result[prime] = max(prime_factors_a.get(prime,0),prime_factors_b.get(prime,0))

    lcm=1
    for prime in result:
        lcm *= prime**result[prime]

    return lcm
print(lcm(18,12))


