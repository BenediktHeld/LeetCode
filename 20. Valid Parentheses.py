class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        NotValid = []
        for i in range(len(s)):
            if (s[i] == "{") or (s[i] == "[") or (s[i] == "("):
                NotValid.append(s[i])  # Füge die öffnende Klammer hinzu
            elif (s[i] == "}") or (s[i] == "]") or (s[i] == ")"):
                if not self.checkIfallreadyCofferd(i, NotValid):  # Überprüfe, ob die Klammer gültig ist
                    return False
                if NotValid:  # Wenn NotValid nicht leer ist
                    last_open = NotValid.pop()  # Entferne die letzte öffnende Klammer
                    if not self.isMatching(last_open, s[i]):  # Überprüfe, ob sie übereinstimmen
                        return False
        return len(NotValid) == 0  # Überprüfe, ob alle Klammern geschlossen wurden

    def checkIfallreadyCofferd(self, i, NotValid):
        # returns True if valid else false
        return True  # Diese Methode wird nicht mehr benötigt, da wir die Logik geändert haben

    def isMatching(self, open_char, close_char):
        # Überprüfe, ob die öffnende und schließende Klammer übereinstimmen
        return (open_char == "{" and close_char == "}") or \
               (open_char == "[" and close_char == "]") or \
               (open_char == "(" and close_char == ")")

# Beispielnutzung
s = "([)]"
solution = Solution()
print(solution.isValid(s))  # Gibt False zurück
