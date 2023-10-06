def reversecomplement(file):
    f = open(file, 'r')
    txt = f.read()
    large_to_small = {'A':'a',
               'T':'t',
               'G':'g',
               'C':'c'
               }
    for key, value in large_to_small.items():
        if key in txt:
            txt = txt.replace(key, value)
    complementary = {'a':'T',
               't':'A',
               'g':'C',
               'c':'G'
               }
    for key, value in complementary.items():
        if key in txt:
            txt = txt.replace(key, value)
    reversecomplementary = txt[::-1].strip()
    newfile = open('PatternRC.txt', 'w')
    newfile.write(reversecomplementary)
    newfile.close()

x = input("Please, write the file's name with '.txt' extension: ")
print(reversecomplement(x))