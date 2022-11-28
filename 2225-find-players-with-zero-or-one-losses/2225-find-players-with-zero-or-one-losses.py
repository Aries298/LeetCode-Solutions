class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = set()
        for p1,p2 in matches:
            players.add(p1)
            players.add(p2)
        values = [0] * len(players)
        losses = dict(zip(players, values))
        for match in matches:
            losses[match[1]] += 1
        no_loss = [num for num, losses in losses.items() if losses == 0]
        one_loss = [num for num, losses in losses.items() if losses == 1]
        return [sorted(no_loss), sorted(one_loss)]