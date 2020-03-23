import math
def sum_divisors(n):
    sum1 = 0
    divisor = 2
    if n == 0:
        return 0
    while divisor <= math.sqrt(n):
        if n % divisor == 0 :
            if (divisor == n/divisor):
                sum1 += divisor
            else:
                sum1 = sum1+ (divisor + n/divisor)
        divisor += 1
    return int(sum1 +1)
   
print(sum_divisors(6)) # Should be 1+2+3=6
print(sum_divisors(12)) # Should be 1+2+3+4+6=16
print(sum_divisors(100))
