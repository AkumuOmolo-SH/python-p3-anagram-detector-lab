# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()  # store lowercase for easier comparison

    def match(self, candidates):
        matches = []
        for candidate in candidates:
            if sorted(candidate.lower()) == sorted(self.word) and candidate.lower() != self.word:
                matches.append(candidate)
        return matches


