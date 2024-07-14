# Leetcode 1859.Sorting the sentence

class Solution:
    def sortSentence(self, s: str) -> str:
         words = s.split()
         indexed_words = []
         for word in words:
            actual_word = word[:-1] 
            index = int(word[-1]) 
            indexed_words.append((actual_word, index))
         indexed_words.sort(key=lambda x: x[1])
         original_words = [word[0] for word in indexed_words]
         original_sentence = " ".join(original_words)

         return original_sentence