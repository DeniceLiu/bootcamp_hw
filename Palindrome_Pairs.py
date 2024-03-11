class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        def is_palindrome(check):
            return check == check[::-1]

        reverse_map = {word[::-1]:i for i, word in enumerate(words)}
        result = set()

        for i, word in enumerate(words):
            for j in range(len(word)+1):
                left = word[:j]
                right = word[j:]

                if is_palindrome(left) and right in reverse_map and reverse_map[right] != i:
                    result.add((reverse_map[right], i))
                
                if is_palindrome(right) and left in reverse_map and reverse_map[left] != i:
                    result.add((i, reverse_map[left]))
        
        return list(result)
