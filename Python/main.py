# With out regex Pattern

import os
from itertools import combinations


# Custom regex matching
def matches_pattern(word, pattern):
    if not pattern:
        return not word
    if len(pattern) == 1 or pattern[1] != '*':
        if not word or (word[0] != pattern[0] and pattern[0] != '.'):
            return False
        return matches_pattern(word[1:], pattern[1:])
    while word and (word[0] == pattern[0] or pattern[0] == '.'):
        if matches_pattern(word, pattern[2:]):
            return True
        word = word[1:]
    return matches_pattern(word, pattern[2:])


# LCS function
def find_lcs(s1, s2):
    m, n = len(s1), len(s2)
    dp = [['' for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(m):
        for j in range(n):
            if s1[i] == s2[j]:
                dp[i + 1][j + 1] = dp[i][j] + s1[i]
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1], key=len)
    return dp[m][n]


# Reading file
with open(os.path.join(os.getcwd(), 'input.txt'), 'r') as file:
    n = int(file.readline())
    words = sorted([file.readline().strip().lower() for _ in range(n)])
    regex_pattern = file.readline().strip().lower()



# o(nlongn) + o(m*n)+ o(n*m*p)
# Matching words
matching_words = [word for word in words if matches_pattern(word, regex_pattern)][:3]
print(matching_words)

# Find the LCS of all permutations of the three words
lcs = ""
max_lcs_length = 0
# for combo in combinations(matching_words, 2):
#     lcs_c = find_lcs(combo[0], combo[1])
#     if len(lcs_c) > max_lcs_length:
#         max_lcs_length = len(lcs_c)
#         lcs = lcs_c

# Finding LCS among first three matching words
lcs = ''
if len(matching_words) > 2:
    lcs12 = find_lcs(matching_words[0], matching_words[1])
    print(lcs12)
    lcs = find_lcs(lcs12, matching_words[2])
    print(lcs)
elif len(matching_words) > 1:
    lcs = find_lcs(matching_words[0], matching_words[1])
elif matching_words:
    lcs = matching_words[0]

# Writing output to file
with open(os.path.join(os.getcwd(), 'output.txt'), 'w') as file:
    file.write(lcs.upper())
