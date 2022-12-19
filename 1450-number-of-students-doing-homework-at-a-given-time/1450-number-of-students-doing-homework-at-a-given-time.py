class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        ans = 0
        for st, et in zip(startTime,endTime):
            if st <= queryTime <= et: ans +=1
        return ans