class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def is_self_dividing(num):
            num = str(num)
            if '0' in num:
                return False
            else:
                for n in num:
                    if int(num) % int(n) != 0:
                        return False
            return int(num)
        
        return [x for x in range(left, right + 1) if is_self_dividing(x)]