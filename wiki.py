import wikipedia
import speech_recognition as sr
r = sr.Recognizer()
mic = sr.Microphone()

wikipedia.set_lang("en")
print("Speak search term")

with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
search_term=r.recognize_google(audio)
print('Searching For ',search_term)

suggested=wikipedia.search(search_term)
x=1
print("Search Results")
for i in suggested:
    print(str(x)+":"+i)
    x=x+1
num=input("Which do you want to search? ")
print(wikipedia.summary(suggested[int(num)-1]))
# print(wikipedia.languages())