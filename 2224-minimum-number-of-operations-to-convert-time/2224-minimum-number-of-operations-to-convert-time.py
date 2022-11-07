class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        curr_hour, curr_minute = int(current[:2]), int(current[3:])
        correct_hour, correct_minute = int(correct[:2]), int(correct[3:])
        ans = abs(correct_hour - curr_hour)
        if curr_minute > correct_minute:
            ans -= 1
        to_add = (correct_minute - curr_minute) % 60
        ans += to_add // 15
        to_add %= 15
        ans += to_add // 5
        to_add %= 5
        ans += to_add // 1
        to_add %= 1
        return ans

        
        