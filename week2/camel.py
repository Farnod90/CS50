user_input = input()

for char in user_input:
    if char.isupper() :
        user_input =  user_input.replace(char, '_' + char.lower())

print(user_input)