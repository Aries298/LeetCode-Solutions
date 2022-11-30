class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        ret = dict()
        for item in items1:
            if item[0] in ret.keys():
                ret[item[0]] += item[1]
            else:
                ret[item[0]] = item[1]
        for item in items2:
            if item[0] in ret.keys():
                ret[item[0]] += item[1]
            else:
                ret[item[0]] = item[1]
        return sorted([[a, b] for a, b in ret.items()])
        