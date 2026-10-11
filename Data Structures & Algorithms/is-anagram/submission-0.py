class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sTable = {}
        tTable = {}
        for i, letter in enumerate(s):
            if sTable.get(letter) != None:
                sTable[letter] += 1
            else:
                sTable[letter] = 0
        for i, letter in enumerate(t):
            if tTable.get(letter) != None:
                tTable[letter] += 1
            else:
                tTable[letter] = 0
        for key in sTable.keys():
            if sTable.get(key) != tTable.get(key):
                return False
        return True