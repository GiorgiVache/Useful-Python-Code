def minimum_skew(genome):
    skew_list = [0]
    for i in range(len(genome)):
        nucleotide = genome[i]
        if nucleotide == 'C':
            skew_list.append(skew_list[-1] - 1)
        elif nucleotide == 'G':
            skew_list.append(skew_list[-1] + 1)
        else:
            skew_list.append(skew_list[-1])
    min_value = min(skew_list)
    index_list = [i for i, x in enumerate(skew_list) if x == min_value]
    index_list_string = ''
    for _ in index_list:
        index_list_string += str(_) + ' '
    return index_list_string.rstrip()

f = open('dataset_30277_10.txt', 'r')
print(minimum_skew(f.read()))
