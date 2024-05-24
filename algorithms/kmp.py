"""
Knuth-Morris-Pratt String-Matching Algorithm

Time Complexity: O(n + k), where n is the length of the word being searched, k is the length of the word to match
Space Complexity: O(k)

Motivation: - The naive or brute-force approach to string matching does a lot of
repeated work.

- For each failed match, typical approaches will then simply go to the next
  index to repeat the search.

- In the work case, this is a costly mistake, meaning those algorithms run in
  O(kn) time, where k is the length of the search word.

KMP approach:

KMP avoids the mistakes of the brute-force selections by employing the
observation that when a mismatch occurs, the word itself embodies sufficient
information to determine where the next match could begin, thus bypassing
re-examination of previously matched characters. 

Overall, it's worst-case time complexity is O(k) + O(n), where O(k) is from
preprocessing of the search word and O(n) is from matching.

algorithm kmp_search:
    input:
        an array of characters, S (the text to be searched)
        an array of characters, W (the word sought)
    output:
        an array of integers, P (positions in S at which W is found)
        an integer, nP (number of positions)

    define variables:
        an integer, j ← 0 (the position of the current character in S)
        an integer, k ← 0 (the position of the current character in W)
        an array of integers, T (the table, computed elsewhere)

    let nP ← 0

    while j < length(S) do
        if W[k] = S[j] then
            let j ← j + 1
            let k ← k + 1
            if k = length(W) then
                (occurrence found, if only first occurrence is needed, m ← j - k  may be returned here)
                let P[nP] ← j - k, nP ← nP + 1
                let k ← T[k] (T[length(W)] can't be -1)
        else
            let k ← T[k]
            if k < 0 then
                let j ← j + 1
                let k ← k + 1

--------------------------------------

algorithm kmp_table:
    input:
        an array of characters, W (the word to be analyzed)
    output:
        an array of integers, T (the table to be filled)

    define variables:
        an integer, pos ← 1 (the current position we are computing in T)
        an integer, cnd ← 0 (the zero-based index in W of the next character of the current candidate substring)

    let T[0] ← -1

    while pos < length(W) do
        if W[pos] = W[cnd] then
            let T[pos] ← T[cnd]
        else
            let T[pos] ← cnd
            while cnd ≥ 0 and W[pos] ≠ W[cnd] do
                let cnd ← T[cnd]
        let pos ← pos + 1, cnd ← cnd + 1

    let T[pos] ← cnd (only needed when all word occurrences are searched)

"""


def kmp_search(S: str, W: str):
    j = 0  # Current position in S
    k = 0  # Current position in W

    P = [0] * len(S)  # Positions in S at which W is found
    nP = 0  # Number of positions

    T = kmp_table(W)  # Prefix table

    while j < len(S):
        if W[k] == S[j]:
            j += 1
            k += 1
            if k == len(W):
                P[nP] = j - k
                nP += 1
                k = T[k]
        else:
            k = T[k]
            if k < 0:
                j += 1
                k += 1

    return (P, nP)


def kmp_table(W: str):
    T = [0] * (len(W) + 1)

    pos = 1  # The current position we are computing in T
    cnd = 0  # The zero-based index in W of the next character of the current candidate substring

    T[0] = -1

    while pos < len(W):
        if W[pos] == W[cnd]:
            T[pos] = T[cnd]
        else:
            T[pos] = cnd
            while cnd >= 0 and W[pos] != W[cnd]:
                cnd = T[cnd]
        pos += 1
        cnd += 1

    T[pos] = cnd

    return T


if __name__ == "__main__":
    S = "foobarfoobarfoobarbaz"
    W = "foobar"

    P, nP = kmp_search(S, W)
    assert nP == 3
    assert P[0] == 0
    assert P[1] == 6
    assert P[2] == 12
