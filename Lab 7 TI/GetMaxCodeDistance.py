from GenerateMatrixes import get_next_word
from collections import defaultdict

def mul(info_word, Gsys, q):
    code_word = []
    for j in range(len(Gsys[0])):
        sum = 0
        for i in range(len(info_word)):
            sum += (info_word[i] * Gsys[i][j]) % q
        code_word.append(sum % q)
    return code_word

def get_min_code_distance(Gsys, info_words, q):
    d = []
    for i in range(1, len(info_words)):
        code_word = mul(info_words[i], Gsys, q)
        d.append(len(code_word) - code_word.count(0))
    d.sort()
    return d[0]

def get_all_min_distances(matrixes, k, q):
    info_words = [[0 for i in range(k)]]
    all_min_distances = defaultdict(list)

    for i in range(1, q**k):
        info_words.append(get_next_word(info_words[i-1], q))
    
    for i in range(len(matrixes)):
        min_code_distance = get_min_code_distance(matrixes[i], info_words, q)
        all_min_distances[min_code_distance].append(i)

    return all_min_distances
