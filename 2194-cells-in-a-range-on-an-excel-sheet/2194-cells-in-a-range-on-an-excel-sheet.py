class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        return [f'{x}{y}' for x in list(map(chr, range(ord(s[0]), ord(s[3])+1))) for y in range(int(s[1]),int(s[4])+1)]