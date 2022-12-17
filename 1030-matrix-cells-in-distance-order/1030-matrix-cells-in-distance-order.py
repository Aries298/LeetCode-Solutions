class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        dist_dict = {}
        for i in range(rows):
            for j in range(cols):
                try:
                    dist_dict[abs(rCenter - i) + abs(cCenter - j)].append([i, j])
                except:
                    dist_dict[abs(rCenter - i) + abs(cCenter - j)] = []
                    dist_dict[abs(rCenter - i) + abs(cCenter - j)].append([i, j])

        dist_dict = {key:dist_dict[key] for key in sorted(dist_dict.keys())}
        ans = []
        for coords_set in dist_dict.values():
            for coords in coords_set:
                ans.append(coords)
        return ans