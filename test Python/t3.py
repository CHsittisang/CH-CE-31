print(" *** Alphabet classification ***")
word = input("Input Sentence to count : ")
vowel_counting = 0
consonant_counting = ""
for i in word :
    if i.lower() in  "aeiou" :
        vowel_counting += 1
    else :
        consonant_counting += i
print("\nvowel in this Sentence is :",vowel_counting)
print("Consonant in this Sentence is :",len(consonant_counting))
# Samantha, Elizabeth, and Joan are on the committee.
