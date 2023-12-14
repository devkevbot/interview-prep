class MySolution:
    def romanToInt(self, s: str) -> int:
        """
        Let n = the length of s
        Time: O(n)
        Space: O(1)
        """
        symbol_table = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        result = 0
        i = 0
        while i < len(s):
            if s[i] == "I" and i + 1 < len(s) and s[i + 1] in ["V", "X"]:
                result += symbol_table[s[i + 1]] - symbol_table[s[i]]
                i += 2
            elif s[i] == "X" and i + 1 < len(s) and s[i + 1] in ["L", "C"]:
                result += symbol_table[s[i + 1]] - symbol_table[s[i]]
                i += 2
            elif s[i] == "C" and i + 1 < len(s) and s[i + 1] in ["D", "M"]:
                result += symbol_table[s[i + 1]] - symbol_table[s[i]]
                i += 2
            else:
                result += symbol_table[s[i]]
                i += 1

        return result


class AlternateSolution:
    def romanToInt(self, s: str) -> int:
        """
        Let n = the length of s
        Time: O(n)
        Space: O(1)
        """
        symbol_table = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        result = 0

        for i in range(len(s) - 1):
            if symbol_table[s[i]] < symbol_table[s[i + 1]]:
                result -= symbol_table[s[i]]
            else:
                result += symbol_table[s[i]]

        return result + symbol_table[s[-1]]
