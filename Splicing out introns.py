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