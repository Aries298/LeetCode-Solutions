class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats, students = sorted(seats), sorted(students)
        return sum([abs(x-y) for x,y in zip(seats, students)])