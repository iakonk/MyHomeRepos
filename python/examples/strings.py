#  find index of substring
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []

        single_len = len(words[0])
        total_len = single_len * len(words)
        words_srt = sorted(words)

        indices = []
        for i in range(0, len(s)):
            slice = s[i: i + total_len]
            if sorted([slice[x:x + single_len] for x in range(0, len(slice), single_len)]) == words_srt:
                indices.append(i)
        return indices

cl = Solution()
assert cl.findSubstring("barfoothefoobarman", ["foo","bar"]) == [0, 9]
cl = Solution()
assert cl.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"]) == []
cl = Solution()
assert cl.findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]) == [6,9,12]


# Create function which calculate list of pairs from list of digits [3, -4, 7, 12, 13,21, 5, 7, -6, 0, 1, 6, 2, -5],
# where sum of each pair equals 7.
# Result list have to looks like this [[X,Y], [X2,Y2], [X3,Y3]]
# without pair duplication such as [5,2] and [2,5].
# Also, evaluate the complexity of implemented function and optimize it if possible.
def find_sum(array, constant, y):
    array = sorted(array)
    lo =0
    hi = len(array)
    while lo <= hi:
        mid = lo + (hi-lo)/2
        if array[mid] + y > constant:
            hi = mid -1
        elif array[mid] + y < constant:
            lo = mid + 1
        else:
            return tuple(sorted([array[mid],y]))

result = set()
arr = [250, 265, 300, 400, 700, -258]
# arr = [200, 265, 265, 265, -258, 265]
# arr = [3, -4, 7, 12, 13, 21, 5, 7, -6, 0, 1, 6, 2, -5]
for i in range(0, len(arr)):
    pair = find_sum(arr, 7, arr[i])
    if pair:
        result.add(pair)
print(result)


# Can you break the given string into words, provided by a given hashmap
#  of frequency of words as <word: n>
hash = {'abc': 3, 'ab': 2, 'abca': 1}
str_ = 'abcabab' # --> No
# hash = {'abc': 3, 'ab':2, 'abca': 1}
# str_ = 'abcabcabcabababca' # --> Yes
for substr, freq_num in hash.iteritems():  # N = hashmap len
        if not len(str_):
            break
        total_len = freq_num * len(substr)
        single_len = len(substr)
        for i in range(0, len(str_)):   # M =string len
            piece = str_[i: i + total_len] # K = piece len
            words = [piece[x: x + single_len] for x in range(0, len(piece), single_len)]
            if words == [substr] * freq_num:
                str_ = str_[:i] + str_[i + total_len:]
if not str_:
    print('Yes')
else:
    print ('No')

# Find whether string S is periodic
# Periodic indicates S = nP
# S=ababab the n=3 and P=ab
# S=xxxxx then n=1 and P=x
string_ = 'ababab'
for single_len in range(1, len(string_)+1):
    words = [string_[x: x+single_len] for x in range(0, len(string_), single_len)]
    # for i in range(0, len(words)):
    #     if fvst

# 9X9, calculate unique pairs
def generate_pairs(x_len, y_len):
    import random
    pairs = set()
    while len(pairs) < 3:
        pair = (random.sample(range(0, x_len), 1)[0], random.sample(range(0, y_len), 1)[0])
        pairs.add(pair)
    return pairs
print(generate_pairs(9, 18))


# Naive string matcher
string_ = 'dsldsf'
substr = 'vl'
for i in range(0, len(string_)):
    piece = string_[i: i+len(substr)]
    for x in range(0, len(piece), len(substr)):
        if piece[x: x + len(substr)] == substr:
            print (i, 'matched')
