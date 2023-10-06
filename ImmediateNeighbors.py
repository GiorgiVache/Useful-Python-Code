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


print(immediate_neighbors('AAGC'))
