class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while sandwiches:
            if sandwiches[0] in students: students.remove(sandwiches.pop(0))
            else: break
        return len(sandwiches)