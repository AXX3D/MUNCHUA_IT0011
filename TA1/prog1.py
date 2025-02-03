def count_characters(input_string):
    vowel_count = 0
    consonant_count = 0
    space_count = 0
    nonletters = 0

    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

    for char in input_string:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1
        elif char == ' ':
            space_count += 1
        else:
            nonlettersnonletters += 1

    print(f"Vowel Count: {vowel_count}")
    print(f"Constonant Count: {consonant_count}")
    print(f"Whitespaces: {space_count}")
    print(f"Non letters: {nonletters}")

textinput = input("Enter your prompt: ")
count_characters(textinput)