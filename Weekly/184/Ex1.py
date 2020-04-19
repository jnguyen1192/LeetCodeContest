class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for word_sub_test in words:
            for word_whole in words:
                if word_sub_test != word_whole and word_sub_test in word_whole:
                    res.append(word_sub_test)
                    break
        if len(res) != 0:
            return res
        return []