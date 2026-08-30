class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # if string size are different length, return false
        if len(s) != len(t):
            return False

        d1,d2 = {},{} # two dictionaries: letter : count

        # for anagram to be true both strings need to have same letter
        # and same number of letters
      

        #.get function for a dict gets the value
        for i in range(len(s)): #only one loop since both str have same size t
            d1[s[i]] = 1 + d1.get(s[i],0) # second paramter is 0 in case key dne
            d2[t[i]] = 1 + d2.get(t[i], 0)
        
        for c in d1:
            if d1[c] != d2.get(c,0):
                return False
        
        return True



