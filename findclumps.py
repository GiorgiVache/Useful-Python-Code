def frequency_table(text, k):
    freqmap = {}
    n = len(text)
    for i in range(n - k):
        pattern = text[i:(i + k)]
        if pattern not in freqmap:
            freqmap[pattern] = 1
        else:
            freqmap[pattern] += 1
    return freqmap


def find_clumps(text, k, L, t):
    f = open(text, 'r')
    genome = f.read()
    patterns = []
    n = len(genome)
    for i in range(n - L):
        window = genome[i:(i + L)]
        freqmap = frequency_table(window, k)
        for key, value in freqmap.items():
            if freqmap[key] >= t:
                patterns.append(key)
    patterns1 = list(dict.fromkeys(patterns))
    return len(patterns1)


x = input("Please, write the file name with 'txt' extension: ")
y = int(input("Please, write k: "))
z = int(input("Please, write L: "))
m = int(input("Please, write t: "))
print(find_clumps(x, y, z, m))
