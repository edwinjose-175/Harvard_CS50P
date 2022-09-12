# strip greeting off leading and trailing whitespaces and convert to lower case for case and space insensitivity
greeting = input("Greeting: ").lower().strip()

if "hello" in greeting:
    print("$0")
elif greeting[0] == "h":
    print("$20")
else:
    print("$100")