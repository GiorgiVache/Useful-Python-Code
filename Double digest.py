import re
dna = open(r'D:\Python for Biologists\exercises and examples\regular_expressions\exercises\dna.txt').read().rstrip('\n')
all_cuts = [0]
for match in re.finditer(r'A[ATGC]TAAT', dna):
    all_cuts.append(match.start() + 3)

for match in re.finditer(r'GC[AG][[AT]TG', dna):
    all_cuts.append(match.start() + 5)

all_cuts.append(len(dna))

sorted_cuts = sorted(all_cuts)
print(sorted_cuts)

for i in range(1, len(sorted_cuts)):
    this_cut_position = sorted_cuts[i]
    previous_cut_position = sorted_cuts[i-1]
    fragment_size = this_cut_position - previous_cut_position
    print('one fragment size is ' + str(fragment_size))