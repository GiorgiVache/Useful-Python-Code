def patternmatch(file):
    f = open(file, 'r')
    lines = f.readlines()
    pattern = lines[0].rstrip()
    genome = lines[1].rstrip()
    patternstarts = []
    rng = len(genome) - len(pattern)
    for i in range(rng):
        end = i + len(pattern)
        if genome[i:end] == pattern:
            patternstarts.append(i)
    patternstartsstring = ''
    for start in patternstarts:
        patternstartsstring = patternstartsstring + str(start) + ' '
    patternstartsstring1 = patternstartsstring.rstrip(' ')
    newfile = open('PatternIndices.txt', 'w')
    newfile.write(patternstartsstring1)
    newfile.close()

x = input("Please, write the file's name with '.txt' extension: ")
print(patternmatch(x))