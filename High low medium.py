data = open('D:\Python for Biologists\exercises and examples\conditional_tests\exercises\data.csv')
for line in data:
    columns = line.rstrip('\n').split(',')
    species = columns[0]
    sequence = columns[1]
    name = columns[2]
    expression = columns[3]
    if ((sequence.upper().count('A') + sequence.upper().count('T'))/len(sequence)) > 0.65:
        print('AT content of ' + name + ' is high')
    elif ((sequence.upper().count('A') + sequence.upper().count('T'))/len(sequence)) < 0.45:
        print('AT content of ' + name + ' is low')
    else:
        print('AT content of ' + name + ' is medium')