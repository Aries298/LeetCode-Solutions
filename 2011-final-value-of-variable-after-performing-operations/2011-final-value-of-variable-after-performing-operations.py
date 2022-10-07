OPERATIONS = {"++X" : 1, "X++" : 1, "--X" : -1, "X--": -1}
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum([OPERATIONS[operation] for operation in operations])