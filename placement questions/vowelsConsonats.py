text='hellow World!'
#setup counters and declaration 
vowel_count=0
consonant_count=0
vowel='aeiouAEIOU'
#loop
for char in text:
    #check ingonore spaces and punctutaion in text
    if char.isalpha():
        #check if the letter is vowel
        if char in vowel:
            vowel_count+=1
        else:
            consonant_count+=1
print('vowel: ',vowel_count)
print('consonat: ',consonant_count)