from googletrans import Translator

translator = Translator()

language = {"bn": "Bangla",
            "en": "English",
            "ko": "Korean",
            "fr": "French",
            "de": "German",
            "he": "Hebrew",
            "hi": "Hindi",
            "it": "Italian",
            "ja": "Japanese",
            'la': "Latin",
            "ms": "Malay",
            "ne": "Nepali",
            "ru": "Russian",
            "ar": "Arabic",
            "zh": "Chinese",
            "es": "Spanish"
            }

allow = True  # variable to control correct language code input


while allow:  # checking if language code is valid

    code_language = input(
        f"Please enter 'options' to view the language conversions. Then select your desired language: \n")

    if code_language == "options":  # showing language options
        print("Code : Language")  # Heading of language option menu
        for i in language.items():
            print(f"{i[0]} => {i[1]}")
        print()  # adding an empty space

    else:  # validating user input
        for lan_code in language.keys():
            if lan_code == code_language:
                print(f"You have selected {language[lan_code]}")
                allow = False
        if allow:
            print("The language you selected is not a valid language code!")

while True:  # starting translation loop
    string = input(
        "\nPlease enter the text you want to translate: \nTo exit the program enter 'close'\n")

    if string == "close":  # exit program command
        print(f"\nThank you for your usage.\nHave a nice Day!")
        break

    # translating method from googletrans
    translated = translator.translate(string, dest=code_language)

    # printing translation
    print(f"\n{language[code_language]} translation: {translated.text}")
    # printing pronunciation
    print(f"Pronunciation : {translated.pronunciation}")

    for i in language.items():  # checking if the source language is listed on language dict and printing it
        if translated.src == i[0]:
            print(f"Translated from : {i[1]}")
