class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3: return 0
        primes = [True] * n
        primes[0] = primes[1] = 0
        m = 2
        while m * m < n:
            if primes[m] == 1:
                primes[m*m:n:m] = [0] * (1 + (n - m * m -1) // m)
            m += 1 if m == 2 else 2
        return sum(primes)
    
        