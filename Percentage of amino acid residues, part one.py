def amino_acid_in_seq(protein_sequence, amino_acid_residue):
    sequence_length = len(protein_sequence)
    amino_acid_quantity = protein_sequence.upper().count(amino_acid_residue.upper())
    the_percentage = (amino_acid_quantity/sequence_length) * 100
    return the_percentage


assert amino_acid_in_seq("MSRSLLLRFLLFLLLLPPLP", "M") == 5
assert amino_acid_in_seq("MSRSLLLRFLLFLLLLPPLP", "r") == 10
assert amino_acid_in_seq("msrslllrfllfllllpplp", "L") == 50
assert amino_acid_in_seq("MSRSLLLRFLLFLLLLPPLP", "Y") == 0
