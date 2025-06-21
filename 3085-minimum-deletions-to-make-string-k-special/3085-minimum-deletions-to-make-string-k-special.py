from collections import Counter

class Solution(object):
    def minimumDeletions(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        freq = Counter(word)
        freq_values = list(freq.values())
        freq_values.sort()
        
        min_deletions = float('inf')

        # Try each unique frequency as the target
        for i in range(len(freq_values)):
            target = freq_values[i]
            deletions = 0
            for f in freq_values:
                if f > target + k:
                    deletions += f - (target + k)
                elif f < target:
                    deletions += f  # delete all occurrences of very small freq chars
            min_deletions = min(min_deletions, deletions)
        
        return min_deletions
