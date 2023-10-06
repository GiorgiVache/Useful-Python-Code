genomic_dna = open('D:\Python for Biologists\exercises and examples\lists_and_loops\exercises\genomic_dna.txt').read()
exon_locations = open('D:\Python for Biologists\exercises and examples\lists_and_loops\exercises\exons.txt')
coding_sequence = ''

for line in exon_locations:
    positions = line.split(',')
    start = int(positions[0])
    stop = int(positions [1])
    exon = genomic_dna[start:stop]
    coding_sequence = coding_sequence + exon
    print('coding sequence is : ' + coding_sequence)

output = open('D:\Python for Biologists\Bioinformatics Finished Exercises\Chapter 4\coding_sequence.txt', 'w')
output.write(coding_sequence)
output.close()