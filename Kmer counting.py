import os
import sys

kmer_size = int(sys.argv[1])
count_cutoff = int(sys.argv[2])

def split_dna(dna, kmer_size):
    kmers = []
    for start in range(0,len(dna)-(kmer_size-1),1):
        kmer = dna[start:start+kmer_size]
        kmers.append(kmer)
    return kmers

kmer_counts = {}

for file_name in os.listdir("."):
    if file_name.endswith(".dna"):
        dna_file = open(file_name)

        for line in dna_file:
            dna = line.rstrip("\n")

            for kmer in split_dna(dna, kmer_size):
                current_count = kmer_counts.get(kmer, 0)
                new_count = current_count + 1
                kmer_counts[kmer] = new_count

for kmer, count in kmer_counts.items():
    if count > count_cutoff:
        print(kmer + " : " + str(count))


