def vowel(n):
    vowel=''
    conconsonants=''
    for char in n.lower():
        if char in 'aeiou':
            vowel=''
        else:
            conconsonants=''
            return conconsonants
    return vowel
print(vowel('swaroop'))
