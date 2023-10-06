def hamming_distance(p, q):
    list1 = list(p)
    list2 = list(q)
    count = 0
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            count += 1
    return count


def suffix(pattern):
    return pattern[1:]


def neighbors(pattern, d):
    nucleotides = ['A', 'T', 'G', 'C']
    if d == 0:
        return [pattern]
    if len(pattern) == 1:
        return nucleotides
    neighborhood = []
    suffix_neighbors = neighbors(suffix(pattern), d)
    for suffix_neighbor in suffix_neighbors:
        if hamming_distance(suffix(pattern), suffix_neighbor) < d:
            for nucleotide in nucleotides:
                neighborhood.append(nucleotide + suffix(pattern))
        else:
            neighborhood.append(pattern[0] + suffix_neighbor)
    return neighborhood


print(neighbors('ACG', 1))
