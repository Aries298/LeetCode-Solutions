class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        time_pairs = sorted(list(zip(plantTime,growTime)),key=lambda x:x[1], reverse=True)
        ans, plant_time = 0, 0
        for plant, grow in time_pairs:
            plant_time += plant
            ans = max(ans, plant_time+grow)
        return ans