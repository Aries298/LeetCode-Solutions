class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        empty_space = sorted([cap-occupied for cap, occupied in zip(capacity, rocks)])[::-1]
        while empty_space and additionalRocks and empty_space[-1] <= additionalRocks:
            additionalRocks -= empty_space.pop()
        return len(rocks) - len(empty_space)