# main.py

from trie import Trie


def lcs_of_three(word1, word2, word3):
    n1, n2, n3 = len(word1), len(word2), len(word3)

    # 3D table for DP
    dp = [[[0 for k in range(n3 + 1)] for j in range(n2 + 1)] for i in range(n1 + 1)]

    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            for k in range(1, n3 + 1):
                if word1[i - 1] == word2[j - 1] == word3[k - 1]:
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                else:
                    dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])

    # Extracting LCS from the dp table
    i, j, k = n1, n2, n3
    lcs_string = []
    while i > 0 and j > 0 and k > 0:
        if word1[i - 1] == word2[j - 1] == word3[k - 1]:
            lcs_string.append(word1[i - 1])
            i -= 1
            j -= 1
            k -= 1
        else:
            max_val = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])
            if max_val == dp[i - 1][j][k]:
                i -= 1
            elif max_val == dp[i][j - 1][k]:
                j -= 1
            else:
                k -= 1

    return ''.join(reversed(lcs_string))


def lcs_of_two(word1, word2):
    n1, n2 = len(word1), len(word2)

    # 2D table for DP
    dp = [[0 for j in range(n2 + 1)] for i in range(n1 + 1)]

    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Extracting LCS from the dp table
    i, j = n1, n2
    lcs_string = []
    while i > 0 and j > 0:
        if word1[i - 1] == word2[j - 1]:
            lcs_string.append(word1[i - 1])
            i -= 1
            j -= 1
        else:
            if dp[i - 1][j] > dp[i][j - 1]:
                i -= 1
            else:
                j -= 1

    return ''.join(reversed(lcs_string))


# Read input
with open("input.txt", "r") as file:
    n = int(file.readline().strip())
    words = [file.readline().strip() for _ in range(n)]
    pattern = file.readline().strip()

# Build the Trie with words
trie = Trie()
for word in words:
    trie.insert(word)

# Find matching words using Trie
matching_words = trie.find_words_matching_pattern(pattern)



print(matching_words)

if len(matching_words) > 2:
    result = lcs_of_three(matching_words[0], matching_words[1], matching_words[2])
elif len(matching_words) == 2:
    result = lcs_of_two(matching_words[0], matching_words[1])
else:
    result = matching_words[0]


# Save result to output.txt
with open("output.txt", "w") as file:
    file.write(result)
