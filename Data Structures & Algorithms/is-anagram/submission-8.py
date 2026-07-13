class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sol 2: put intto hashtable O(n*m) is time complexity
        map_s = {}
        for char in s:
            if map_s.get(char):
                map_s[char] += 1
            else:
                map_s[char] = 1
        
        map_t = {}
        for char in t:
            if map_t.get(char):
                map_t[char] += 1
            else:
                map_t[char] = 1 
            
        return map_s == map_t
