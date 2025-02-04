import text_to_speech
import speech_to_text
import datetime 
import webbrowser
#import weather

def Action (data):
    user_data = data.lower()

    if "what is your name" in user_data:
        text_to_speech.text_to_speech("My name is virtual assistant")
        return "My name is virtual assistant"

    elif "hello" in user_data or "hey" in user_data or "hi" in user_data:
        text_to_speech.text_to_speech("hey , sir How can i help you")
        return "hey , sir How can i help you"

    elif "good morning" in user_data:
        text_to_speech.text_to_speech("good morning sir ")
        return "good morning sir "

    elif "time now" in user_data():
        current_time = datetime.datetime.now()
        Time = (str)(current_time) + "Hour :" , (str)(current_time.minute) + "Minute"
        text_to_speech.text_to_speech(Time)
        return Time


    elif "shutdown" in user_data:
        text_to_speech.text_to_speech("ok sir")
        return"ok sir"

    elif "play music" in user_data:
        webbrowser.open("https://spotify.com/")
        text_to_speech.text_to_speech("spotify.com is now ready for you")
        return "spotify.com is now ready for you"

    elif "open youtube" in user_data:
        webbrowser.open("https://youtube.com/")
        text_to_speech.text_to_speech("youtude.com is now ready for you")
        return "youtude.com is now ready for you"

    elif "open google" in user_data:
        webbrowser.open("https://google.com/")
        text_to_speech.text_to_speech("google.com is now ready for you")
        return "google.com is now ready for you"

    #elif "weather" in user_data:
        #ans = weather.weather()
        #text_to_speech.text_to_speech(ans)
        #return ans

    else:
        text_to_speech.text_to_speech("I'm not able to understand")
        return "I'm not able to understand"




