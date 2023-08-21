import regex
import os
from itertools import combinations

# Reading file
with open(os.path.join(os.getcwd(), 'input.txt'), 'r') as file:
    n = int(file.readline())
    words = [file.readline().strip().lower() for _ in range(n)]
    regex_pattern = file.readline().strip().lower()

# Matching words
matching_words = sorted([word for word in words if regex.fullmatch(regex_pattern, word)])

# Selecting the first three words
selected_words = matching_words[:3]

# Finding the longest common subsequence
def find_lcs(s1, s2):
    matrix = [["" for j in range(len(s2))] for i in range(len(s1))]
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                if i > 0 and j > 0:
                    matrix[i][j] = matrix[i-1][j-1] + s1[i]
                else:
                    matrix[i][j] = s1[i]
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1], key=len)

    cs = matrix[-1][-1]

    return cs

# Find LCS for any two combinations and then find LCS with third one
if len(selected_words) == 3:
    lcs_two = find_lcs(selected_words[0], selected_words[1])
    lcs = find_lcs(lcs_two, selected_words[2])
elif len(selected_words) == 2:
    lcs = find_lcs(selected_words[0], selected_words[1])
else:
    lcs = selected_words[0] if selected_words else ''

# Writing output to file
with open(os.path.join(os.getcwd(), 'output.txt'), 'w') as file:
    file.write(lcs.upper())
