# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pyaudio
p = pyaudio.PyAudio()
num = p.get_device_count()
input_device = []
output_device = []
for i in range(0,num):
    device = p.get_device_info_by_index(i)
    if(device.maxInputChannels > 0):
        print("Output index:", output_device[i].index)
        print("name:", output_device[i].name)
    elif(device.maxOutputChannels > 0):
        print("Output index:", output_device[i].index)
        print("name:", output_device[i].name)


