

sentence=input('Enter any sentence ')

vowel_count={
'a':0,
'e':0,
'i':0,
'o':0,
'u':0
}

for i in sentence:
    if i in vowel_count:
        vowel_count[i]+= 1
total_vowels= sum(vowel_count.values())
print(total_vowels)
