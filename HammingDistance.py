def hamming_distance(p, q):
    list1 = list(p)
    list2 = list(q)
    count = 0
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            count += 1
    return count

f = open('dataset_30278_3.txt', 'r')
lines = f.readlines()
sequence1 = lines[0].strip()
sequence2 = lines[1].strip()
print(hamming_distance(sequence1, sequence2))