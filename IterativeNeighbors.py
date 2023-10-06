def immediate_neighbors(pattern):
    neighborhood = [pattern]
    nucleotides = ['A', 'T', 'G', 'C']
    for i in range(len(pattern)):
        symbol = pattern[i]
        for nucleotide in nucleotides:
            if symbol != nucleotide:
                neighbor = pattern[:i] + nucleotide + pattern[(i + 1):]
                neighborhood.append(neighbor)
    return neighborhood


def iterative_neighbors(pattern, d):
    neighborhood = [pattern]
    for i in range(1, d):
        for pattern1 in neighborhood:
            neighborhood.append(immediate_neighbors(pattern1))
    return neighborhood


print(iterative_neighbors('ACG', 2))
