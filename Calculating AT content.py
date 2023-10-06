# Calculating AT content

dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
count_A = dna.count("A")
count_T = dna.count("T")
length_dna = len(dna)
proportion_AT = (count_A+count_T)/length_dna
print("AT content is " + str(proportion_AT))
