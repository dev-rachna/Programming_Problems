'''
30. Substring with Concatenation of All Words

You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input:
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
Output: []
'''
import collections


def findSubstring(s, words):
    wordBag = collections.Counter(words)
    wordLen = len(words[0])
    substrLen = wordLen*len(words)
    res = []

    for j in range(len(s)-substrLen+1):
        seen = collections.defaultdict(int)

        for i in range(j, j+substrLen, wordLen):
            word = s[i:i+wordLen]
            if word in wordBag:

                seen[word] += 1
                if seen[word] > wordBag[word]:
                    break
            else:
                break

        if seen == wordBag:
            res.append(j)
    return res
