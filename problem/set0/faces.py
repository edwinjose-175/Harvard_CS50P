def convert(text):
    slightly_smiling_face = "🙂"
    slighlty_frowning_face = "🙁"
    return text.replace(":)", slightly_smiling_face).replace(":(", slighlty_frowning_face)

def main():
    user_text = input()
    converted_text = convert(user_text)
    print(converted_text)

main()