import math
class Solution:
    def waysToBuildRooms(self, p: List[int]) -> int:
        def aux(l):
            sum_l = sum(l)
            l.sort(reverse=True)
            i = l[0]
            a = 1
            for j in range(1, len(l)):
                for k in range(l[j]):
                    a *= (i+k+1)
                a = a//math.factorial(l[j])
                i += l[j]
                a = a%(10**9+7)
            return a
        
        n = len(p)
        if n == 2:
            return 1
        d_chil = {}  # dict of children 
        for i in range(1, n):
            if p[i] in d_chil.keys():
                d_chil[p[i]] += [i]
            else:
                d_chil[p[i]] = [i]
        
        d_n_chil = {}# dict of how many children a node has + 1(itself)
        def find_n_chil(idx):
            if idx not in d_chil.keys():
                d_n_chil[idx] = 1
                return 1
            a = 0
            for i in range(len(d_chil[idx])):
                a += find_n_chil(d_chil[idx][i])
            d_n_chil[idx] = a+1
            return a+1
        
        find_n_chil(0)
        
        def count_ways(idx):
            if idx not in d_chil.keys():
                return 1
            l = d_chil[idx]
            if len(l) == 1:
                return count_ways(l[0])
            else:
                a = 1
                s = []
                for i in l:
                    a *= count_ways(i)
                    a = a%(10**9+7)
                    s += [d_n_chil[i]]
                a *= aux(s)
                return a%(10**9+7)
        return count_ways(0)