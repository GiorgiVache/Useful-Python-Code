data = open('D:\Python for Biologists\exercises and examples\conditional_tests\exercises\data.csv')
for line in data:
    columns = line.rstrip('\n').split(',')
    species = columns[0]
    sequence = columns[1]
    name = columns[2]
    expression = columns[3]
    if (name.startswith('k') or name.startswith('h')) and not species=='Drosophila melanogaster':
        print(name)