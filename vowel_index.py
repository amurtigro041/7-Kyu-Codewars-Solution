def vowel_indices(word):
    list_alphab = list(word)
    vowels = ['a','i','u','e','o','A','I', 'U','E','O','y','Y']
    index_result = []
    i = 0
    for x in list_alphab:
        if x in vowels:
            index_result.append(i + 1)  
        i += 1

    return index_result

print(vowel_indices('Apple'))
print(vowel_indices('supercalifragilisticexpialidocious'))