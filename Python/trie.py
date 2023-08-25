# Trie.py

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False
        self.word = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end_of_word = True
        node.word = word

    def find_words_matching_pattern(self, pattern, max_results=3):
        results = []
        self._search(self.root, "", pattern, results)
        return results[:max_results]

    def _search(self, node, current_word, pattern, results):
        if not node or len(results) >= 3:
            return

        if node.end_of_word and self.is_match(current_word, pattern):
            results.append(current_word)

        for char, child_node in node.children.items():
            self._search(child_node, current_word + char, pattern, results)

    def is_match(self, s, p):
        n, m = len(s), len(p)
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True

        for i in range(n + 1):
            for j in range(1, m + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2] or (i > 0 and (s[i - 1] == p[j - 2] or p[j - 2] == '.') and dp[i - 1][j])
                else:
                    dp[i][j] = i > 0 and dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '.')

        return dp[n][m]
