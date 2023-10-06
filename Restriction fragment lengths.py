# Restriction fragment lengths

dna = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
half_1 = dna.find('GAATTC') + 1
half_2 = len(dna) - half_1
print('length of first fragment is ' + str(half_1))
print('length of second fragment is ' + str(half_2))