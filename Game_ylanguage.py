#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 20:48:41 2019

@author: apple
"""

import sys,time,cv2,face_recognition,dlib,pyaudio
import pygame
import model_recognize,faceswap
import viVoicecloud as vv
p = pyaudio.PyAudio()
vv.Login()
t = vv.tts()

ASR = vv.asr()
tr = vv.baidu_translate()
t = vv.tts()

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
Sample_channels = 1
Sample_rate = 16000
Sample_width = 2
time_seconds = 0.5
stream = p.open(
        rate = Sample_rate,
        format = p.get_format_from_width(Sample_width),
        channels = Sample_channels,
        input = True,
        input_device_index = device_in,
        start = False)

img = cv2.imread("self1.jpg")
tags=[]
faces=[]

self3_img = face_recognition.load_image_file("self3.jpg")
#print(face_recognition.face_encodings(self3_img))
cbn3 = face_recognition.face_encodings(self3_img)[0]
faces = faces+[cbn3]
tags = tags+["cbn3"]
print("ok1")

while True:
    try:
        t.say(text = "欢迎来到游语游戏AI王国，下面请你准备识别面部，进入游戏", voice = "nannan")
        print("欢迎来到游语游戏诶爱王国，下面请你准备识别面部，进入游戏")
        cap = cv2.VideoCapture(0)
        width = 640
        height = 480
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        print("ok2")
        ret, frame = cap.read()#reading pictures from cam
        img = frame      
        t1 = time.time()
        names = face_recognition.face_encodings(img)
        face_locations = face_recognition.face_locations(img)
        flag = 0   
        for i in range(len(names)):
            faceCompare = face_recognition.compare_faces(faces,names[i], tolerance = 0.5)#higher, preciser
            try:
                faceIndex = faceCompare.index(True)
                print("Name:",tags[faceIndex])
                t.say(text = "welcome championNan", voice = "John")
                print("欢迎楠楠小朋友")
                print("ok3")
                if flag == 0:
                    cv2.imwrite("capture_self.jpg", img)
                    flag = flag+1
                cap.release()
                #第一阶段面部识别部分完成
                print("说出你的选择1.游语学习2.为图像做装饰3.换脸4.标出特征点并画框5.姿态识别6.退出")
                while True:
                    ASR.SessionBegin(language = 'Chinese')
                    stream.start_stream()
                    t.say(text = "说出你的选择:游语学习或为你自己的识别捕捉图像做一些小装饰或退出", voice = "nanan")
                    status = 0
                    while status!= 3: #其他返回值的使用？
                        frames = stream.read(int(Sample_rate*time_seconds), exception_on_overflow = False)
                        ret, status, recStatus = ASR.AudioWrite(frames)
                    stream.stop_stream()
                    print('*识别中...*')
                    words = ASR.GetResult()#识别说话人的语句
                    #print("TYPE:", type(words))
                    ASR.SessionEnd()
                    print("*识别结果*",words)
                    pygame.mixer.init()
                    track = pygame.mixer.Sound("shuohuahaowan.wav")
                    track.play()
                    time.sleep(2)#等录音完成后
                    if(words == '游语学习。'):
                        while(1):
                            flag = 0
                            print("下面请听录音打印出游语的翻译，若正确则会提示真实的读法,难度依次上升,最后输出你的总成绩")
                            translate = input("level1:")
                            pygame.mixer.init()
                            track = pygame.mixer.Sound("yunvwugua.wav")
                            time.sleep(1)#避免多个识别冲突
                            track.play()
                            time.sleep(2)
                            if(translate == "雨女无瓜"):
                                t.say(text = "与你无关", voice = "xiaofeng")
                                flag += 1
                            translate = input("level2:")
                            pygame.mixer.init()
                            track = pygame.mixer.Sound("tazazhegeyazi.wav")
                            time.sleep(1)#避免多个识别冲突
                            track.play()
                            time.sleep(2)#等录音完成后
                            if(translate == "怎么会变成现在这个亚子"):
                                t.say(text = "怎么会变成现在这个样子", voice = "yanping")
                                flag += 1
                            translate = input("level3:")
                            pygame.mixer.init()
                            track = pygame.mixer.Sound("zuihouweishenmoyazi.wav")
                            time.sleep(1)#避免多个识别冲突
                            track.play()
                            time.sleep(3)#等录音完成后
                            if(translste == "其实最后他为什么会变成那个亚子"):
                                t.say(text = "其实最后他为什么会变成那个样子", voice = "yanping")
                                flag += 1
                            print("score:", flag)
                            print("请说出你是否想继续玩当前游戏:")
                            ASR.SessionBegin(language = 'Chinese')
                            stream.start_stream()
                            t.say(text = "说出你的选择:游语学习或为你自己的识别捕捉图像做一些小装饰或退出", voice = "nanan")
                            status = 0
                            while status!= 3: #其他返回值的使用？
                                frames = stream.read(int(Sample_rate*time_seconds), exception_on_overflow = False)
                                ret, status, recStatus = ASR.AudioWrite(frames)
                            stream.stop_stream()
                            print('*识别中...*')
                            words = ASR.GetResult()#识别说话人的语句
                            #print("TYPE:", type(words))
                            ASR.SessionEnd()
                            print("*识别结果*",words)
                            pygame.mixer.init()
                            track = pygame.mixer.Sound("shuohuahaowan.wav")
                            track.play()
                            time.sleep(2)#等录音完成后
                            if(words == '返回。'):
                                break
                            if(words == '退出。'):
                                sys.exit(0)
                    elif(words == '为图像做装饰。'):
                        try_import.model_recognize()#戴上圣诞帽，老师提供的代码
                    elif(words == '换脸。'):
                        faceswap.switch_face()
                    elif(words == '标出特征点并画框。'):
                        detector = dlib.get_frontal_face_detector()
                        landmark_predictor = dlib.shape_predictor('/Users/apple/Desktop/sjtu/shape_predictor_5_face_landmarks.dat')
                        img = cv2.imread('/Users/apple/Desktop/sjtu/self1 copy.jpg')
                        faces = detector(img,1)
                        if (len(faces) > 0):
                            for k,d in enumerate(faces):
                                cv2.rectangle(img,(d.left(),d.top()),(d.right(),d.bottom()),(255,255,255))
                                shape = landmark_predictor(img,d)
                                for i in range(5):
                                    cv2.circle(img, (shape.part(i).x, shape.part(i).y),5,(0,255,0), -1, 8)
                                    cv2.putText(img,str(i),(shape.part(i).x,shape.part(i).y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,2555,255))
                        cv2.imshow('Frame',img)
                        cv2.waitKey(0)
                   # elif(words == '姿态识别。'):
                        
                    elif(words == '退出。'):
                        sys.exit(0) 
                    else:
                        t.say(text = "不好意思，没有听清你的要求，您能再说一次吗", voice = "jinger")
                        print("为听清要求，再说一遍")
                
            except Exception as e:
                print("error in capturing:", e)
                t.say(text = "你是没有识别过的小朋友呢，不能未经大人容许玩这个游戏呢", voice = "jinger")
                print("没有记录在档案中")
                pygame.mixer.init()
                track1 = pygame.mixer.Sound("changexiaop.wav")
                time.sleep(1)#避免多个识别冲突
                track1.play()
                print("OOPS游戏被家长中断了",e)
                cap.release()
                    
    except Exception as e:
        if(e == KeyboardInterrupt):
            t.say(text = "熊孩子又偷玩游戏",voice = "yanping")
            pygame.mixer.init()
            track_f = pygame.mixer.Sound("changexiaop.wav")
            track_f.play()
            time.sleep(5)
            print("OOPS游戏被家长中断了",e)
            cap.release()
            vv.Logout()
            sys.exit(0)
        else:
            print("Terminate by unrecognition:", e)
            t.say(text = "请小朋友扭扭头，没有拍到你呢", voice = "nannan")
            cap.release()
        


    
    

