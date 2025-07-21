def count_vowels(string):
    count = 0
    for char in string:
        # if vowel == 'a' or vowel == 'A' or vowel == 'e' or vowel == 'E' or vowel == 'i' or vowel == 'I' or vowel == 'o' or vowel == 'O' or vowel == 'u' or vowel == 'U': # very verbose
        #     count = count + 1
        if char.lower() in ['a', 'e', 'i', 'o', 'u']: # more pythonic
            count += 1

    return count

text = "The weather is windy today."
count = count_vowels(text)
print(count)
