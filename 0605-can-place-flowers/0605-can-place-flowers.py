class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) < 3:
            if sum(flowerbed) == 0:
                return 1 >= n
            else:
                return 0 >= n
        ans = 0
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            ans += 1
            flowerbed[0] = 1
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            ans += 1
            flowerbed[-1] = 1
        for i in range(1,len(flowerbed)-1):
            if not flowerbed[i-1] and not flowerbed[i] and not flowerbed[i+1]:
                ans += 1
                flowerbed[i] = 1
        return ans >= n
            