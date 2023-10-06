# Complementing DNA

dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
dna_1=dna.replace('A','t')
dna_2=dna_1.replace('T','a')
dna_3=dna_2.replace('G','c')
dna_4=dna_3.replace('C','g')
print(dna_4.upper())