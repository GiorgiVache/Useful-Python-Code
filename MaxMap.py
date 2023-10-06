def maxmap(file):
    frequentpatterns = []
    worddict = {}
    f = open(file, 'r')
    lines = f.readlines()
    txt = lines[0].strip()
    k = int(lines[1].strip())
    rng = len(txt) - k
    for i in range(rng):
        end = i + k
        pattern = txt[i:end]
        if pattern in worddict:
            worddict[pattern] += 1
        else:
            worddict[pattern] = 1
    max_count = max(worddict.values())
    for key, value in worddict.items():
        if worddict[key] == max_count:
            frequentpatterns.append(key)
    string_of_patterns = ''
    for pttrn in frequentpatterns:
        string_of_patterns += pttrn + ' '
    string_of_patterns1 = string_of_patterns.rstrip(' ')
    return string_of_patterns1

x = input("Please, write the file's name with '.txt' extension: ")
print(maxmap(x))