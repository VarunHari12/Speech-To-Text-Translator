from googletrans import Translator, constants
from pprint import pprint
import speech_recognition as sr

print("Welcome to the language translator!")

r = sr.Recognizer()
translator = Translator()

with sr.Microphone() as source:
    print("Please say what you want to translate: ")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
except:
    print("I was not able to hear what you said.")
    exit()
    
langs = list(constants.LANGUAGES.values())
codes = list(constants.LANGUAGES.keys())
langDict = {}
# print(langs)

for i in range(0,len(langs)):
    langDict.update({langs[i]:codes[i]})

# print(langDict)
    

while True:
    languageTarget = input("What language would you like to translate to today? (Type \"help\" to see a list of supported languages): ")
    

    if languageTarget.lower() == "help":
        print("Total supported languages:", len(constants.LANGUAGES))
        print("Languages:")
        pprint(langs)
    else:
        break

# languageSource = input("What language are you speaking in today: ")


try:
    translation = translator.translate(text, dest = langDict[languageTarget])
except ValueError:
    print("Invalid language. Please use the abbreviated form.")
except:
    print("An error has occured")
else:
    print(translation.text)
    
