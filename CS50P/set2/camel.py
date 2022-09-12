camel = input("camelCase: ")

# empty string
snake = ''

# case: single name
if camel.islower():
    snake = camel
# case: camel case input
else:
    for letter in camel:
        if letter.isupper():
            snake = snake + f"_{letter.lower()}"
        else:
            snake = snake + letter
print(snake)