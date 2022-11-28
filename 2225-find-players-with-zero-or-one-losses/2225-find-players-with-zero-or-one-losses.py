class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = set()
        for p1,p2 in matches:
            players.add(p1)
            players.add(p2)
        losses = dict(zip(players, [0] * len(players)))
        for match in matches:
            losses[match[1]] += 1
        return [sorted([num for num, losses in losses.items() if losses == 0]), sorted([num for num, losses in losses.items() if losses == 1])]