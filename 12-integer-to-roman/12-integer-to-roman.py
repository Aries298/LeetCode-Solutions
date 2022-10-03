class Solution:
    def intToRoman(self, num: int) -> str:
        THOUSANDS = ("","M","MM","MMM","MMMM")
        HUNDREDS = ("","C","CC","CCC","CD","D","DC","DCC","DCCC","CM")
        TENS = ("","X","XX","XXX","XL","L","LX","LXX","LXXX","XC")
        ONES = ("","I","II","III","IV","V","VI","VII","VIII","IX")
        
        ORDER = (ONES,TENS,HUNDREDS,THOUSANDS)
        
        ans = ""
        num = str(num)
        
        for i in range(len(num)):
            idx = int(num[-i-1])
            ans = ORDER[i][idx] + ans
        return ans