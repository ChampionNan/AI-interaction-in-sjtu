#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 15:55:09 2019

@author: apple
"""
import wave,pyaudio

file_name = "output.wav"

wf = wave.open(file_name, 'rb')

Sample_channels = wf.getnchannels()
Sample_rate = wf.getframerate()
Sample_width = wf.getsampwidth()
Output_index = 3

nframes = wf.getnframes()
frames = wf.readframes(nframes)

wf.close()

p = pyaudio.PyAudio()

stream = p.open(
        rate = Sample_rate,
        format = p.get_format_from_width(Sample_width),
        channels = Sample_channels,
        output = True,
        output_device_index = Output_index,
        start = True)
stream.write(frames)

stream.stop_stream()
stream.close()
p.terminate()


