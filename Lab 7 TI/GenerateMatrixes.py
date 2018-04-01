from itertools import product, combinations_with_replacement, permutations, combinations
from copy import deepcopy
import numpy as np
from Gauss import Gauss

def get_next_word(prev_word, q):
    k = len(prev_word)
    new_word = prev_word.copy()
    for i in range(k-1,-1,-1):
        if new_word[i] + 1 < q:
            new_word[i] += 1
            for j in range(i+1, k): new_word[j] = 0
            break
    return new_word

def get_identity_matrix(k):
    identity_matrix = []
    for i in range(k):
        identity_matrix.append([1 if j == i else 0 for j in range(k)])
    return identity_matrix

def Plotkin(n, k, q):
    return int(n*(q**(k-1))*(q-1)/(q**k - 1))

def get_ends(n, k, q, d0):
    ends = []
    for d in range(d0-1, n-k):
        sets = list(combinations_with_replacement([i for i in range(1, q)], d))
        for i in range(len(sets)):
            current_set = list(sets[i])
            current_set.extend([0 for i in range(n-k-len(current_set))])
            current_ends = list(permutations(current_set, n-k))
            for end in current_ends:
                ends.append(list(end))
    return ends

def check_linear_independence(matrix, n, k, q):
    arr = np.matrix(matrix)
    rank = np.linalg.matrix_rank(matrix)
    kek = rank==len(matrix)
    if kek==True:
        return kek
    if k > n-k: 
        if rank == len(matrix) - (k - n + k): 
            return True
    return False

def add(row1, row2, q):
    new_row = []
    for i in range(len(row1)):
        new_row.append((row1[i]+row2[i])%q)
    return new_row

def check_strings(matrix, k, q, d0):
    pairs = combinations([i for i in range(0,k)], 2)
    for pair in pairs:
        sum = add(matrix[pair[0]], matrix[pair[1]], q)
        zeros = sum.count(0)
        if len(sum) - zeros < d0 - 2:
            return False

def check(item, d0):
    zeros = item.count(0)
    return len(item) - zeros >= d0-1

def get_dmin_list(n, k, q):
    return [i for i in range(Plotkin(n,k,q), 0, -1)]

def get_all_matrixes(n,k,q):
    all_matrixes = []
    E = get_identity_matrix(k)
    dmin_list = get_dmin_list(n, k, q)
    d0 = 1

    for d in dmin_list:
        if d < n-k:
            continue
        if d == n-k:
            dmin = d-1
            break
    print(d0)

    #ends = get_ends(n, k, q, d0)
    ends = [[0 for i in range(n-k)]]
    for i in range(1,q**(n-k)):
        ends.append(get_next_word(ends[i-1], q))
    i = 0
    while True:
        if i>= len(ends):
            break

        if check(ends[i], d0) == False:
            ends.pop(i)
            continue
        i += 1
    print(ends)

    #for item in product(ends, repeat=k):
    #    new_matrix = deepcopy(E)
    #    for i in range(k):
    #        new_matrix[i].extend(item[i])
    #    all_matrixes.append(new_matrix)
    #return all_matrixes
    
    #for d in range(d0-1, n-k):
    #    sets = list(combinations_with_replacement([i for i in range(1, q)], d))
    #    for i in range(len(sets)):
    #        current_set = list(sets[i])
    #        current_set.extend([0 for i in range(n-k-len(current_set))])
    #        current_ends = list(permutations(current_set, n-k))
    #        for end in current_ends:
    #            ends.append(list(end))

    p_parts = list(permutations(ends, k))
    for p_part in p_parts:
        if k>n-k:
            checker = check_strings(list(p_part), k, q, d0) == False
        else: 
            checker = check_linear_independence(list(p_part), n, k, q) == False or check_strings(list(p_part), k, q, d0) == False
        if checker == True:
            continue
        new_matrix = deepcopy(E)
        for i in range(k):
            new_matrix[i].extend(p_part[i])
        all_matrixes.append(new_matrix)
        break
    return all_matrixes
