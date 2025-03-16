def shell(file, numLines, newfile=None):
    reader = open(file, 'r')
    writer = open(newfile, 'w')

    i = 0
    for line in reader:
        if i < numLines:
            writer.write(line)
            i += 1
        else:
            break

    reader.close()
    writer.close()


shell('pg345.txt', 5, 'bingo.txt')
