def hamming_distance(p, q):
    list1 = list(p)
    list2 = list(q)
    count = 0
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            count += 1
    return count


def pattern_matching_count(pattern, genome, d):
    count = 0
    for i in range(len(genome) - len(pattern) + 1):
        end = i + len(pattern)
        if hamming_distance(genome[i:end], pattern) <= int(d):
            count += 1
    return count

f = open('dataset_30278_6.txt', 'r')
lines = f.readlines()
PATTERN = lines[0].strip()
GENOME = lines[1].strip()
D = lines[2].strip()
print(pattern_matching_count(PATTERN, GENOME, D))
