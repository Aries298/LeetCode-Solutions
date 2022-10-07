class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return [(i % 3 == 0) * 'Fizz' + (i % 5 == 0) * 'Buzz' if (i % 3 == 0 or i % 5 == 0) else str(i) for i in range(1,n+1)]