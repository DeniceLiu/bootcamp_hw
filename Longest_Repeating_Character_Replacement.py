class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        max_len = 0
        max_count = 0
        count = {}

        start = 0
        for end in range(len(s)):
            count[s[end]] = count.get(s[end], 0) + 1
            max_count = max(max_count, count[s[end]])

            while(end-start+1)-max_count > k:
                count[s[start]] -= 1
                start += 1
            
            max_len = max(max_len, end-start+1)
        
        return max_lens
