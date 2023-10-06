sequences = open("input.txt")
output = open('D:\Python for Biologists\Bioinformatics Finished Exercises\Chapter 4\ trimmed.txt', 'w')
for line in sequences:
    trimmed_line = line[14:]
    output.write(trimmed_line)
    print(str(len(trimmed_line)))
output.close()
