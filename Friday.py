from __future__ import print_function

from ctypes import *

import ex1_kwstest as kws
import ex4_getText2VoiceStream as gt2v
import ex2_getVoice2Text as gv2t
import MicrophoneStream as MS
import user_auth as UA
import time
import Briefe as bf
import weather_inform

   
def main():
    KWSID = ['기가지니', '지니야', '친구야', '자기야']
    exit_keyword = "종료"
    
    while True:
        recog = kws.test(KWSID[0])
        print(recog)
        if recog == 200:
            print("호출어 인식성공 \n STT 명령 시작...")
            MS.play_file("./data/start.wav")
            while True:
                command = gv2t.getVoice2Text()
                if exit_keyword in command:
                    MS.play_file('./data/exit_sound.wav')
                    break
                else:
                    bf.action(command)
    
        
if __name__ == "__main__":
    main()
