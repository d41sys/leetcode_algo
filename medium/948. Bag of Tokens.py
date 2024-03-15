class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        if tokens == []:
            return 0
        if (len(tokens) == 1):
            if (power < tokens[0]):
                return 0
            else:
                return 1
        tokens.sort()
        score = 0
        while (len(tokens) >= 1):
            if power < tokens[0]:
                return score
            score = score + 1   
            power = power - tokens[0]
            tokens.remove(tokens[0])
            if (len(tokens) == 1 and power < tokens[0]) or (len(tokens) == 0):
                return score
            if power < tokens[0] and score >= 1:
                power = power + tokens[len(tokens)-1]
                score = score - 1
                tokens.remove(tokens[len(tokens)-1])
        return score