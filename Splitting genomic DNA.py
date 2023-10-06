# Splicing out introns

genomic_dna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
exon_1 = genomic_dna[0:63]
exon_2 = genomic_dna[90:]
print(exon_1+exon_2)

genomic_dna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
exon_1 = genomic_dna[0:63]
exon_2 = genomic_dna[90:]
dnaweget=exon_2+exon_1
percentageofthedna=(len(dnaweget)/len(genomic_dna))*100
print('The percentage of the DNA sequence coding is ' + str(percentageofthedna)+ '%')

genomic_dna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
exon_1 = genomic_dna[0:63]
intron = genomic_dna[63:90].lower()
exon_2 = genomic_dna[90:]
DNA=exon_1 + intron + exon_2
print(DNA)

dna_file = open("genomic_dna.txt")
my_dna = dna_file.read()
Exon_1 = my_dna[0:63]
Intron = my_dna[63:90]
Exon_2 = my_dna[90:]
coding_DNA = open("coding_dna.txt", "w")
non_coding_DNA = open("noncoding_dna.txt", "w")
coding_DNA.write(Exon_1 + Exon_2)
non_coding_DNA.write(Intron)
