class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        # can be solve with 2n
        # we check every string of s 
        # and every sting of t
        # In the dictionary, when we iterate "s",
        # dict[key] = dict[key]+1 start
        #  when we iterate t
        #  check if value in s 
        #  No return false
        # Yes next step
        # dict[key] = dict[key]-1
        # if dict[key] = 0
        # pop dict.pop(key) 
        # keep iterate until end
        # if it all went through return true
        if len(s) != len(t): 
            return False

        for item in s:
            if item in seen:
                seen[item] = seen[item]+1
            else :
                seen[item] = 1
        print(seen)
        for item in t:
            if item in seen:
                seen[item] = seen[item]-1
                print(seen[item])
                if seen[item] < 1:
                    seen.pop(item)
            else :
                return False
        
        return True
        