# strip answer off whitespaces and convert to lower case for case and space insensitivity
deep_answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()


match deep_answer:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")