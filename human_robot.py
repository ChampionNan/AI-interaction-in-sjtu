#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 23:24:31 2019

@author: apple
"""
import pyaudio,sys
import viVoicecloud as vv
import urllib, json, vlc, time
import urllib.request

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

def aiui_answer(q, vv, tts):
    a = vv.aiui(q)
    if a[0] != 4:
        if a[1] in ["openQA", "datetime", "weather", "calc", "bike", "poetry", "news"]:
            for i in a[3]:
                tts.say(i)

        elif a[1] == "musicX":
            tts.say("暂时未添加音乐模块")

        else:
            tts.say("对不起，这个问题有点难，无对应结果")
    else:
        tts.say("对不起， 没有这样的问题，回答不了")

myqa = {
        "你好":"你好！跟我聊聊吧",
        "你叫什么":"我叫南瓜AI",
        "再见":"行吧，下次再聊吧"
        }

def my_answer(q, tts):
    for key in myqa:
        if key in q:
            tts.say(myqa[key])
            return True
    #print("False return")
    return False


while(1):
    try:
        ASR.SessionBegin(language = 'Chinese')
        stream.start_stream()
        print("*请说出你想选择的功能（1.点歌 2.对话 3.翻译 4.退出）*")
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
        if(words == '退出。'):
            print("*程序终止*")
            vv.Logout()
            stream.close()
            #p.terminate()
            sys.exit(0)
        if(words == '点歌。'):
            while(1):
                url = "http://tingapi.ting.baidu.com/v1/restserver/ting?"
                url += "from=webapp_misic"
                url += "&method=baidu.ting.search.catalogSug"
                url += "&format=json"
                print("**请输入歌曲的关键字按照如下现实的格式:**")
                keywords = input("**歌手 歌曲名:**")
                keywords_encoded = urllib.parse.quote(keywords)
                url += "&query="+keywords_encoded
                ref = urllib.request.urlopen(url)   
                result = ref.read()
                json_str1 = str(result, encoding = 'utf-8')
                dict1 = json.loads(json_str1)
                songid = dict1["song"][0]["songid"]
                url2 = "http://music.taihe.com/data/music/fmlink?"
                url2 += "songIds="+songid   
                ref2 = urllib.request.urlopen(url2)
                result2 = ref2.read()
                dic2 = json.loads(str(result2, encoding = 'utf-8'))
                songLink = dic2['data']['songList'][0]['songLink']
                p = vlc.MediaPlayer(songLink)
                p.play()
                time.sleep(2)
                flag = 0#判断是否为暂停条件，这样才能不退出循环
                
                while p.is_playing() or flag:
                    #音乐播放环节：定位在当前歌曲
                    ASR.SessionBegin(language = 'Chinese')
                    stream.start_stream()
                    print('***说出暂停或继续或退出（退出对当前歌曲的操作）***')
                    status2 = 0
                    while status2 != 3: #其他返回值的使用？
                        frames = stream.read(int(Sample_rate*time_seconds), exception_on_overflow = False)
                        ret, status2, recStatus = ASR.AudioWrite(frames)
                    stream.stop_stream()
                    print('Get Result...')
                    words1 = ASR.GetResult()
                    print(words1)
                    ASR.SessionEnd()
                    if(words1 == '退出。'):
                        p.stop()
                        p.release()
                        break
                    if(words1 == '暂停。'):#暂时停止歌曲，可以在当前循环中继续请求播放-不行，歌曲状态改变了循环不了
                        p.pause()
                        flag = 1
                    if(words1 == '继续。'):
                        p.play()
                        flag = 0
                    time.sleep(0.5)
                #识别语音（返回）判断是否继续停留在音乐模块
                ASR.SessionBegin(language = 'Chinese')
                stream.start_stream()
                print('**请回答是否返回上一级主目录:返回或其他**')
                status3 = 0
                while status3 != 3: #其他返回值的使用？
                    frames = stream.read(int(Sample_rate*time_seconds), exception_on_overflow = False)
                    ret, status3, recStatus = ASR.AudioWrite(frames)

                stream.stop_stream()
                print('**识别中...**')
                words2 = ASR.GetResult()
                ASR.SessionEnd()
                print("**识别结果**", words2)
                if(words2 == '返回。'):
                    break #退出音乐播放模块
        elif(words == '对话。'):
            while(1):
                ASR.SessionBegin(language = 'Chinese')
                stream.start_stream()
                print("**说出交流问答语句或返回或退出:**")
                status4 = 0
                while status4!= 3: #其他返回值的使用？
                    frames = stream.read(int(Sample_rate*time_seconds), exception_on_overflow = False)
                    ret, status4, recStatus = ASR.AudioWrite(frames)
                    
                stream.stop_stream()
                print('**识别中...**')
                words3 = ASR.GetResult()#识别说话人的语句
                ASR.SessionEnd()
                print("**",words3,"**")#识别的功能分类
                if(words3 == "退出。"):
                    print("*程序终止*")
                    vv.Logout()
                    stream.close()
                    #p.terminate()
                    sys.exit(0)
                elif(words3 == "返回。"):
                    break
                elif(my_answer(str(words3), t)):
                    print("这是南瓜AI的回答")
                else:
                    print("这是百度AI的回答")
                    aiui_answer(str(words3),vv,t)
            
        elif(words == '翻译。'):
            while(1):
                ASR.SessionBegin(language = 'Chinese')
                stream.start_stream()
                print("**请说出你想翻译的内容或返回或退出:**")
                status5 = 0
                while status5 != 3: #其他返回值的使用？
                    frames = stream.read(int(Sample_rate*time_seconds), exception_on_overflow = False)
                    ret, status5, recStatus = ASR.AudioWrite(frames)
                    
                stream.stop_stream()
                print('**识别中...**')
                words = ASR.GetResult()#识别说话人的语句
                ASR.SessionEnd()
                try:
                    print("你说的话是:",words)
                    if(words == '返回。'):
                        break
                    if(words == "退出。"):
                        print("*程序终止*")
                        vv.Logout()
                        stream.close()
                        #p.terminate()
                        sys.exit(0)
                    result = tr.translate(words, "zh", "en")
                    print("翻译的结果:",result)
                    print(result)
                    t.say(text = result, voice = "John")
                except Exception as e:
                    print(e)
                    print("**没有识别出请再说一遍**")
            
        elif(words == '退出。'):
            print("*程序终止*")
            vv.Logout()
            stream.close()
            #p.terminate()
            sys.exit(0)
        else:
            print("*无法识别你所说的功能，请尝试再说一遍*") #无识别结果
    except Exception as e:
        print(e)
        print('*程序被强制中断*')
        vv.Logout()
        stream.close()
        #p.terminate()
        sys.exit(0)
