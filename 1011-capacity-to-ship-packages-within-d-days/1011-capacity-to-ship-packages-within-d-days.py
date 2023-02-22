class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def isEnough(capacity):  #helper function, to check if given capacity is enough
            count = 1
            max_weight = capacity
            for weight in weights:
                if weight > max_weight:
                    max_weight = capacity
                    count += 1
                max_weight -= weight
            return True if count <= days else False

        left, right = max(weights), sum(weights)
        while left < right:
            mid = left + (right - left) // 2
            if isEnough(mid):
                right = mid
            else:
                left = mid + 1
        return left