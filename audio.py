#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 22:26:02 2019

@author: apple
"""
def findDevice(name, type):
    p = pyaudio.PyAudio()
    num = p.get_device_count()
    for i in range(0,num):
        device = p.get_device_info_by_index(i)
        if(device.maxInputChannels > 0 and type == 'input' 
           and device['name'] == name):
            return device['index']       
        elif(device.maxOutputChannels > 0 and type == 'output'
             and device['name'] == name):
            return device['index']
            
