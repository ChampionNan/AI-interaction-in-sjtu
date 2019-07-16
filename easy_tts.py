#!/usr/bin/python3
# coding: utf-8
import os
from pypinyin import lazy_pinyin, TONE3
from pydub import AudioSegment

silent = AudioSegment.silent(duration=500)

PINYIN_VOICE_PATH = '/home/pi/work/python_tts/pinyin/16000'

EXPORT_PATH = '/home/pi'
'''
def load_voice_dict():
    voice_file_list = [f for f in os.listdir(PINYIN_VOICE_PATH) if f.endswith('.wav')]
    voice_dict = {}
    
    for voice_file in voice_file_list:
        name = voice_file[:-4]
        song = AudioSegment.from_wav(os.path.join(PINYIN_VOICE_PATH, voice_file))
        voice_dict.setdefault(name, song)
    return voice_dict

        if piny_song is None and piny and piny[-1] not in '0123456789':
            piny = piny + '5'
            piny_song = VOICE_DICT.get(piny, silent)

VOICE_DICT = load_voice_dict()
'''
def txt_to_voice(text, name='test'):
    pinyin_list = lazy_pinyin(text, style=TONE3)
    new = AudioSegment.empty()
    for pinyin in pinyin_list:
        try:
        	pinyin_audio = AudioSegment.from_wav(os.path.join(PINYIN_VOICE_PATH,pinyin+'.wav'))
        
        except:
                print('silence error')
        	pinyin_audio = silent
        #更改crossfade， 以及间隙的添加
        crossfade = min(len(new), len(pinyin_audio + silent), 2500)/60
        new = new.append(pinyin_audio, crossfade=crossfade)
        new = new.append(silent, crossfade = 0)
    
    new.export(os.path.join(EXPORT_PATH, "{}.wav".format(name)), format='wav')
    

if __name__ == '__main__':
    text = u'吃葡萄不吐葡萄皮'
    filename = 'test'
    txt_to_voice(text,filename)
    os.system('play ~/test.wav')
