class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        ergebnis = False
        for i in range(len(magazine)-len(ransomNote)+1):
           if magazine[i:(i+len(ransomNote))]==ransomNote:
               ergebnis = True
               return ergebnis
        return False

Note = "aa"
magazine = "baa"

print(Solution.canConstruct(1,Note,magazine))


