class Solution:
    def letterCombinations(self, digits: str):
        if not digits:
            return []

        # Mapping von Ziffern zu Buchstaben
        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        combinations = []

        def backtrack(index: int, path: str):
            # Wenn der Pfad die Länge der Ziffern erreicht, füge ihn zur Kombination hinzu
            if index == len(digits):
                combinations.append(path)
                return

            # Hole die Buchstaben, die der aktuellen Ziffer entsprechen
            possible_letters = phone_map[digits[index]]
            for letter in possible_letters:
                # Rekursiv den nächsten Buchstaben hinzufügen
                backtrack(index + 1, path + letter)

        # Starte die Backtracking-Funktion
        backtrack(0, "")
        return combinations