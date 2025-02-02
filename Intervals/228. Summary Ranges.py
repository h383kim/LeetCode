################################################################
# Difficulty: Easy
# Problem Link: https://leetcode.com/problems/summary-ranges/
################################################################

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # Base Case
        if len(nums) == 0:
            return []

        # Initialize Streak
        streak_s, streak_e = nums[0], nums[0]
        res = []
        for i in range(1, len(nums)):
            # If the streak breaks
            if nums[i] != nums[i - 1] + 1:
                if streak_s == streak_e:
                    Range = f'{streak_s}'
                else:
                    Range = f'{streak_s}->{streak_e}'

                res.append(Range)
                # Re-initialize streak interval
                streak_s, streak_e = nums[i], nums[i]
            # If the streak goes on just increase the end
            else:
                streak_e = nums[i]
                
        # Remaining interval after breaking the loop
        if streak_s == streak_e:
            Range = f'{streak_s}'
        else:
            Range = f'{streak_s}->{streak_e}'
        res.append(Range)

        return res