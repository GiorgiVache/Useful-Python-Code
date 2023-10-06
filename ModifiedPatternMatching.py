def modifiedpatternmatch(file, pattern):
    f = open(file, 'r')
    genome = f.read()
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
y = input("Please, write the pattern you want to search for: ")
y1 = str(y)
print(modifiedpatternmatch(x, y1))