def patterncount(text, pattern):
    count = 0
    rng = len(text) - len(pattern)
    for i in range(rng):
        end = i + len(pattern)
        if text[i:end] == pattern:
            count += 1
    return count

def frequentwords(file, k):
    frqntpttrns = []
    worddic = {}
    f = open(file, 'r')
    txt = f.read()
    rng = len(txt) - k
    for i in range(rng):
        end = i + k
        pattern = txt[i:end]
        worddic[pattern] = patterncount(txt, pattern)
    maxcount = max(worddic.values())
    for key ,value in worddic.items():
        if worddic[key] == maxcount and key not in frqntpttrns:
            frqntpttrns.append(key)
    return frqntpttrns

x = input("Please, write the file's name with '.txt' extension: ")
y = int(input("Please, write the desired kmer length: "))
print(frequentwords(x, y))