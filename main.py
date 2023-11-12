from googletrans import Translator, constants
from pprint import pprint

translator = Translator()

print("Welcome to the language translator!")


while True:
    language = input("What language would you like to translate to today? (Type \"help\" to see a list of supported languages)")

    if language.lower() == "help":
        print("Total supported languages:", len(constants.LANGUAGES))
        print("Languages:")
        pprint(constants.LANGUAGES)
    else:
        break

text = input("Please input the text you would like to translate: ")   

try:
    translation = translator.translate(text, dest = language)
except ValueError:
    print("Invalid language. Please use the abbreviated form.")
except:
    print("An error has occured")
else:
    print(translation.text)