def amino_acid_in_seq(protein, aa_list = ['A', 'I', 'L', 'M', 'F', 'W', 'Y', 'V']):
    protein = protein.upper()
    protein_length = len(protein)
    total = 0
    for aa in aa_list:
        aa = aa.upper()
        aa_count = protein.count(aa)
        total = total + aa_count
    percentage = (total * 100)/protein_length
    return percentage

assert amino_acid_in_seq("MSRSLLLRFLLFLLLLPPLP", ["M"]) == 5
assert amino_acid_in_seq("MSRSLLLRFLLFLLLLPPLP", ['M', 'L']) == 55
assert amino_acid_in_seq("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L']) == 70
assert amino_acid_in_seq("MSRSLLLRFLLFLLLLPPLP") == 65
