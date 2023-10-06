def hamming_distance(p, q):
    list1 = list(p)
    list2 = list(q)
    count = 0
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            count += 1
    return count


def pattern_matching(pattern, genome, d):
    index_string = ''
    for i in range(len(genome) - len(pattern) + 1):
        end = i + len(pattern)
        if hamming_distance(genome[i:end], pattern) <= int(d):
            index_string += str(i) + ' '
    return index_string.rstrip()


f = open('dataset_30278_4.txt', 'r')
lines = f.readlines()
PATTERN = lines[0].strip()
GENOME = lines[1].strip()
D = lines[2].strip()
new_file = open('Approximate Matches.txt', 'w')
new_file.write(pattern_matching(PATTERN, GENOME, D))
new_file.close()
