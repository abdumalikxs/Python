def palindrome(word):
    for i in range(len(word) // 2):
        if word[i] != word[len(word) - i - 1]:
            return False
        return True


print(palindrome('lolol'))

Bign