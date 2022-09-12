user_input = input("Input: ")

vowels = ['a', 'e', 'i', 'o', 'u']

print("Output: ", end='')

for letter in user_input:
    if letter.lower() in vowels:
        continue
    else:
        print(letter, end='')
print()