#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 16:10:11 2019

@author: apple
"""
import pyaudio

Sample_channels = 1
Sample_rate = 16000
Sample_width = 2

p = pyaudio.PyAudio()

stream = p.open(
        rate = Sample_rate,
        format = p.get_format_from_width(Sample_width),
        channels = Sample_channels,
        input = True,
        output = True,
        input_device_index = 6,
        output_device_index = 3)

print("* Begin:")
stream.start_stream()
frames = stream.read(Sample_rate*5)
stream.write(frames)
print("* done")
stream.stop_stream()#录音
stream.close()
p.terminate()
