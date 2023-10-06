def skew(genome):
    skew_list = [0]
    for i in range(len(genome)):
        nucleotide = genome[i]
        if nucleotide == 'C':
            skew_list.append(skew_list[-1] - 1)
        elif nucleotide == 'G':
            skew_list.append(skew_list[-1] + 1)
        else:
            skew_list.append(skew_list[-1])
    skew_list_string = ''
    for _ in skew_list:
        skew_list_string += str(_) + ' '
    return skew_list_string.rstrip(' ')


print(skew('GAGCCACCGCGATA'))
