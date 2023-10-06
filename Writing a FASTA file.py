header_1 = "ABC123"
header_2 = "DEF456"
header_3 = "HIJ789"
seq_1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"
seq_2 = "actgatcgacgatcgatcgatcacgact"
seq_3 = "ACTGAC-ACTGT--ACTGTA----CATGTG"

output = open("sequences.fasta", "w")
output.write(">" + header_1 + "\n" + seq_1 + "\n")
output.write(">" + header_2 + "\n" + seq_1.upper() + "\n")
output.write(">" + header_1 + "\n" + seq_1.replace("-","") + "\n")