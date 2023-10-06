def patterncount(file):
    f = open(file, 'r')
    lines = f.readlines()
    txt = lines[0].strip()
    pttrn = lines[1].strip()
    count = 0
    rng = len(txt) - len(pttrn)
    for i in range(rng):
        end = i + len(pttrn)
        if txt[i:end] == pttrn:
            count += 1
    return count

x = input("Please, write the file's name with '.txt' extension: ")
print(patterncount(x))