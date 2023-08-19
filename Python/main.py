# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import re
import os
from itertools import combinations





# Defining a function to find LCS
def find_lcs(X, Y):
    m = len(X)
    n = len(Y)
    dp = [[0] * (n + 1) for i in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Constructing LCS
    lcs = ""
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs = X[i - 1] + lcs
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return lcs





def print_hi():
    # Reading file
    with open(os.path.join(os.getcwd(), 'input.txt'), 'r') as file:
        n = int(file.readline())
        words = [file.readline().strip().lower() for _ in range(n)]
        regex_pattern = file.readline().strip().lower()

    # Matching words
    matching_words = [word for word in words if re.fullmatch(regex_pattern, word)]

    # Selecting the first three words
    selected_words = matching_words[:3]

    # Finding LCS of at most three matching words
    lcs = ""
    for comb in combinations(selected_words, 2):
        lcs = max(lcs, find_lcs(*comb), key=len)

    # Writing output to file
    with open(os.path.join(os.getcwd(), 'output.txt'), 'w') as file:
        file.write(lcs.upper())




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
