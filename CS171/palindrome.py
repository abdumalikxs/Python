def rev(word):
    word = word.lower()
    i = 0
    while i < len(word) // 2:
        if word[i] != word[len(word)-i-1]:
            return False
        i += 1
    return True


print(rev('aAaAa'))
####ORRRR

def palindrome(word):
    for i in range(len(word) // 2):
        if word[i] != word[len(word) - i - 1]:
            return False
        return True


print(palindrome('lolol'))
