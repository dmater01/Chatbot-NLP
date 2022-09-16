# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import openai
import pyttsx3
import speech_recognition as sr
import pyaudio
from api_secret import API_KEY

openai.api_key = API_KEY

#initalize the text -2-speech engine
engine = pyttsx3.init('nsss')

#initalize the speech recongnition engine
r =sr.Recognizer()

#initailize the microphone
mic = sr.Microphone(device_index=0)
#Note: #devcie_index is howto determine which microphone to be used.
#to find microphone on the system , see below
print(sr.Microphone.list_microphone_names())


#Intrgrate context into the conversation
conversation = ""

user_name = "Terry"

# set up input audio source loop
while True:
    with mic as source:
        print("Listening .......")
        r.adjust_for_ambient_noise(source,duration=.02)
        audio = r.listen(source)
    print("No Longer Listening")

    try:
        user_input = r.recognize_google(audio)
    except:
        continue
    print(user_input)
    prompt = user_name + ": " + user_input + "\nbot:"
    conversation += prompt
    print(conversation)
    response = openai.Completion.create(
            model="text-davinci-002",
            prompt=conversation,
            temperature=0.9,
            max_tokens=60,
            top_p=1.0,
            frequency_penalty=0.5,
            presence_penalty=0.0,
            stop=["Terry:"]
            )
    #response = openai.Completion.create(engine="text-davinci-002", prompt=conversation,max_tokens=350,temperature=1)
    # In order to get response into a string
    response_str = response['choices'][0]['text'].replace("\n,", "")

    response_str = response_str.split(user_name + ": ",1)[0].split("bot:", 1)[0]

    conversation += response_str + "\n"
    print(conversation)
    engine.say(response_str)
    engine.runAndWait()


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
