import re
accessions = ['xkn59438', 'yhdck2', 'eihd39d9', 'chdsye847', 'hedle3455', 'xjhd53e', '45da', 'de37dp']
for accession in accessions:
    if re.search(r'5', accession):
        print(accession)

accessions = ['xkn59438', 'yhdck2', 'eihd39d9', 'chdsye847', 'hedle3455', 'xjhd53e', '45da', 'de37dp']
for accession in accessions:
    if re.search(r'[de]', accession):
        print(accession)

accessions = ['xkn59438', 'yhdck2', 'eihd39d9', 'chdsye847', 'hedle3455', 'xjhd53e', '45da', 'de37dp']
for accession in accessions:
    if re.search(r'd.*e', accession):
        print(accession)

accessions = ['xkn59438', 'yhdck2', 'eihd39d9', 'chdsye847', 'hedle3455', 'xjhd53e', '45da', 'de37dp']
for accession in accessions:
    if re.search(r'd[^\d]e', accession):
        print(accession)

accessions = ['xkn59438', 'yhdck2', 'eihd39d9', 'chdsye847', 'hedle3455', 'xjhd53e', '45da', 'de37dp']
for accession in accessions:
    if re.search(r'd.*e', accession) or re.search(r'e.*d', accession):
        print(accession)

accessions = ['xkn59438', 'yhdck2', 'eihd39d9', 'chdsye847', 'hedle3455', 'xjhd53e', '45da', 'de37dp']
for accession in accessions:
    if re.search(r'^[xy]', accession):
        print(accession)

accessions = ['xkn59438', 'yhdck2', 'eihd39d9', 'chdsye847', 'hedle3455', 'xjhd53e', '45da', 'de37dp']
for accession in accessions:
    if re.search(r'^[xy].*e$', accession):
        print(accession)

accessions = ['xkn59438', 'yhdck2', 'eihd39d9', 'chdsye847', 'hedle3455', 'xjhd53e', '45da', 'de37dp']
for accession in accessions:
    if re.search(r'[\d]{3,}]', accession):
        print(accession)

accessions = ['xkn59438', 'yhdck2', 'eihd39d9', 'chdsye847', 'hedle3455', 'xjhd53e', '45da', 'de37dp']
for accession in accessions:
    if re.search(r'd[arp]$', accession):
        print(accession)