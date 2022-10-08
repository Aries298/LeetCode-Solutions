class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        boxes = {}
        for number in range(lowLimit, highLimit + 1):
            index = sum([int(x) for x in str(number)])
            try:
                boxes[index] += 1
            except:
                boxes[index] = 1
        return max(boxes.values())