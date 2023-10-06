data = open('D:\Python for Biologists\exercises and examples\conditional_tests\exercises\data.csv')
for line in data:
    columns = line.rstrip('\n').split(',')
    species = columns[0]
    sequence = columns[1]
    name = columns[2]
    expression = columns[3]
    if ((sequence.count('A')+sequence.count('T'))/(len(sequence))<0.5) and int(expression)>200:
        print(name)