vowels = ['a','e','i','o','u']

word = input('input: ')

for i in word:
    if i.lower() in vowels:
        word = word.replace(i,'')
        
print('output:',word)
