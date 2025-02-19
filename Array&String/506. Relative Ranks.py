################################################################
# Difficulty: Easy
# Problem Link: https://leetcode.com/problems/relative-ranks/
################################################################



class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse=True)
        init = max(len(score) + 1, 4)
        placements = list(range(1, init))
        placements[0], placements[1], placements[2] = 'Gold Medal', 'Silver Medal', 'Bronze Medal'
        score_dict = {}
        for i in range(len(score)):
            score_dict[sorted_score[i]] = placements[i]

        answer = []
        for i in range(len(score)):
            answer.append(str(score_dict[score[i]]))
        
        return answer