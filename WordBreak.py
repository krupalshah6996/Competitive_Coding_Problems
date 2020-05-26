class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        answer = [True]
        wordDict = set(wordDict)
        for i in range(1, len(s)+1):
            answer.append(any(answer[j] and s[j:i] in wordDict for j in range(i)))
        # print(answer)
        return answer[-1]