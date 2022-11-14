class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1, num2 = num1.split('+'), num2.split('+')
        num1_real, num1_img = int(num1[0]), int(num1[1][:-1])
        num2_real, num2_img = int(num2[0]), int(num2[1][:-1])
        real_part = num1_real * num2_real - num1_img * num2_img
        img_part = num1_real * num2_img + num2_real * num1_img
        return f'{real_part}+{img_part}i'
        
