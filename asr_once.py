#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 23:24:31 2019

@author: apple
"""
import pyaudio
import viVoicecloud as vv
#from sjtu.audio import findDevice

def findDevice(name, type):
    p = pyaudio.PyAudio()
    num = p.get_device_count()
    for i in range(0,num):
        device = p.get_device_info_by_index(i)
        if(device['maxInputChannels'] > 0 and type == 'input' 
           and device['name'] == name):
            return device['index']       
        elif(device['maxOutputChannels'] > 0 and type == 'output'
             and device['name'] == name):
            return device['index']
            

device_in = findDevice("ac108", "input")
#print(device_in)
Sample_channels = 1
Sample_rate = 16000
Sample_width = 2
time_seconds = 0.5

p = pyaudio.PyAudio()
stream = p.open(
        rate = Sample_rate,
        format = p.get_format_from_width(Sample_width),
        channels = Sample_channels,
        input = True,
        input_device_index = device_in,
        start = False)

vv.Login()
ASR = vv.asr()
ASR.SessionBegin(language = 'Chinese')

stream.start_stream()
print('***Listening')

status = 0
while status!= 3:
    frames = stream.read(int(Sample_rate*time_seconds))
    ret, status, recStatus = ASR.AudioWrite(frames)
    
stream.stop_stream()
print('--GetResult...')
print(recStatus)
words = ASR.GetResult()
ASR.SessionEnd()
print(words)
vv.Logout()
stream.close()
p.terminate()
