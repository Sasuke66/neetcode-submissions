from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        target = "balloon"
        input_text = Counter(text)
        target_text = Counter(target)
        limits = [
            input_text[letter] // target_text[letter]
            for letter in target
        ]
        return min(limits)