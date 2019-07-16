#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 15:40:57 2019

@author: apple
"""
import pyaudio,wave

Sample_channels = 1
Sample_rate = 16000
Sample_width = 2
Input_index = 6

p = pyaudio.PyAudio()

stream = p.open(
        rate = Sample_rate,
        format = p.get_format_from_width(Sample_width),
        channels = Sample_channels,
        input = True,
        input_device_index = Input_index,
        start = False)

print("* recording")
stream.start_stream()
frames = stream.read(Sample_rate*5)
print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

file_name = "output.wav"

wf = wave.open(file_name, 'wb')
wf.setnchannels(Sample_channels)
wf.setsampwidth(Sample_width)
wf.setframerate(Sample_rate)
wf.writeframes(frames)
wf.close()