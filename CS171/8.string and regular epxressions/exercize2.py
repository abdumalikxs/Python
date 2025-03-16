import re
#8.12.5. Exercise

#The Count of Monte Cristo is a novel by Alexandre Dumas that is considered a classic. Nevertheless, in the introduction of an English translation of the book, the writer Umberto Eco confesses that he found the book to be “one of the most badly written novels of all time”.

#In particular, he says it is “shameless in its repetition of the same adjective,” and mentions in particular the number of times “its characters either shudder or turn pale.”

#To see whether his objection is valid, let’s count the number number of lines that contain the word pale in any form, including pale, pales, paled, and paleness, as well as the related word pallor. Use a single regular expression that matches any of these words. As an additional challenge, make sure that it doesn’t match any other words, like impale – you might want to ask a virtual assistant for help.import re


def monte(file):
    linesEncountered = 0
    pattern = "pales|pale|paled|paleness|pallor"
    
    reader = open(file, 'r')
    for line in reader:
        result = re.search(pattern, line)
        if result != None:
            linesEncountered += 1
    reader.close()
    return linesEncountered


