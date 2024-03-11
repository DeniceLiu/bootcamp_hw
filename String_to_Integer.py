class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 32-bit
        MAX_INT = 2**31-1
        MIN_INT = -2**31

        s = s.lstrip() # trim

        if not s:
            return 0
        
        sign = 1
        if s[0] == '-' or s[0] == '+':
            sign = -1 if s[0] == '-' else 1
            s = s[1:]
        
        result = 0
        for char in s:
            if not char.isdigit():
                break
            
            result = result*10+int(char) # add digit

            if result > MAX_INT:
                return MAX_INT if sign == 1 else MIN_INT
        
        return sign*result
