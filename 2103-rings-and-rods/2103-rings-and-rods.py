class Solution:
    def countPoints(self, rings: str) -> int:
        rings = [rings[i:i + 2] for i in range(0, len(rings), 2)]
        rods = dict()
        for ring in rings:
            try:
                rods[ring[1]] += ring[0]
            except:
                rods[ring[1]] = ring[0]
        
        ans = 0
        for rod_num, rings_colours in rods.items():
            if "R" in rings_colours and "G" in rings_colours and "B" in rings_colours:
                ans += 1
        return ans