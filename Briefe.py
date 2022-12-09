import MicrophoneStream as MS
import ex4_getText2VoiceStream as gt2v
import weather_inform

def action(text):
    keyword_1="교통"
    keyword_2="날씨"
    keyword_3="일정"
    keyword_4="뉴스"

    if (keyword_1 in text):
        print("교통정보 알려드림")
        MS.play_file("./data/yes_sound.wav")
        gt2v.getText2VoiceStream("교통정보 알려줄게.", "./reply_sound.wav")
        MS.play_file("./reply_sound.wav")
    elif (keyword_2 in text):
        print("날씨 알려드림")
        MS.play_file("./data/yes_sound.wav")
        gt2v.getText2VoiceStream(weather_inform.getWeather(), "./reply_sound.wav")
        MS.play_file("./reply_sound.wav")
 
    elif (keyword_3 in text):
        print("")
        MS.play_file("./data/yes_sound.wav")    
    elif (keyword_4 in text):
        print("")
        MS.play_file('./data/yes_sound.wav')
    else:
        MS.play_file("./data/reQuery_sound.wav")
