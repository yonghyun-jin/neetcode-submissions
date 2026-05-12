class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26

        # initialize counts for s1 and the first window of s2
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        # initial matches: how many chars have equal counts
        matches = 0
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            # include s2[r] in the window
            idx = ord(s2[r]) - ord('a')
            s2Count[idx] += 1
            if s1Count[idx] == s2Count[idx]:
                matches += 1
            elif s1Count[idx] + 1 == s2Count[idx]:
                matches -= 1

            # exclude s2[l] from the window
            idx = ord(s2[l]) - ord('a')
            s2Count[idx] -= 1
            if s1Count[idx] == s2Count[idx]:
                matches += 1
            elif s1Count[idx] - 1 == s2Count[idx]:
                matches -= 1

            l += 1

        return matches == 26