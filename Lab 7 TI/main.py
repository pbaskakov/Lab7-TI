from GenerateMatrixes import get_all_matrixes
from GetMaxCodeDistance import get_all_min_distances

if __name__ == '__main__':
    n, k, q = [int(value) for value in input('Enter n, k, q: ').split()]
    matrixes = get_all_matrixes(n, k, q)
    all_min_distances = get_all_min_distances(matrixes, k, q)
    keys = list(all_min_distances.keys())
    keys.sort(reverse = True)
    file = open('{},{}.txt'.format(n, k), 'w')

    for key in keys:
        file.write(('{}\nМАТРИЦЫ, ДЛЯ КОТОРЫХ d = {}\n\n'.format('_'*50, key)))
        for i in all_min_distances[key]:
            for row in matrixes[i]:
                file.write('{}\n'.format(row))
            file.write('\n')

    file.close()