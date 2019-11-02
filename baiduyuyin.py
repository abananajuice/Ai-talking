#coding:utf-8
from aip import AipSpeech
from requests import get
from pyaudio import PyAudio,paInt16
import wave
from requests import post
from json import dumps
from playsound import playsound

#import time
from time import sleep
from configparser import ConfigParser


APP_ID = '***'
API_KEY = '****'
SECRET_KEY = '****'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
CHUNK = 1024              #wav文件是由若干个CHUNK组成的，CHUNK我们就理解成数据包或者数据片段。1024
FORMAT = paInt16          #这个参数后面写的paInt16表示我们使用量化位数 16位来进行录音。
CHANNELS = 1              #代表的是声道，这里使用的单声道。 1
RATE = 16000
sampwidth=2

def ping():  #检查网络连接（如果不能则不能使用语音合成功能）
    try:
        html =get("http://www.baidu.com",timeout=2)
        if str(html)!= '<Response [200]>':
            print('question')
            check_net=False
        else:
            check_net=True
    except:
        check_net=False
        print("请检查网络连接")
    return check_net


def LuYin(b):   #录音功能

    # 采样率16k
    #RECORD_SECONDS = Time    #采样时间
    WAVE_OUTPUT_FILENAME = 'recode.wav'   #输出文件名
    a='b'
    if eval(a) == 0:
        a = '5'
    if eval(a)!=0:
        p = PyAudio()
        # 可以在此写一个判断，当如某个值开始录音。最好可以该进程按下录音
        stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
        print("*录音开始*")

        frames = []
        for i in range(0,int(RATE/CHUNK*(eval(a)+1))):
            data = stream.read(CHUNK)
            frames.append(data)
        print(data)
        print("* 录音结束")

        stream.stop_stream()
        stream.close()
        p.terminate()          #关闭数据流，并关闭pyaudio


    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')     #以二进制模式写入
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(sampwidth)
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
#LuYin()
#print(baidu_speech_reco()

def baidu_speech_reco():   #语音识别
    try:
        with open('recode.wav  ', 'rb') as fp:
            results=fp.read()
            result = client.asr(results, 'wav', 16000, {'dev_pid': 1536, })  #联网进行语音识别，返回字典类型
            print(result)
            if 'result'  in result.keys():
                return str(result['result'][0])
            else:
                return '系统提示：语音识别出现问题，请检查'
    except:
        return '系统提示：语音识别出现问题，请检查'
#print(baidu_speech_reco())
def baidu_voice(voice):    #语音合成
    try:
        result= client.synthesis(voice, 'zh', 1, {
            'vol': 5,'per':0
        })
        # 判断返回的是否是二进制的语音，若返回的是字典型则说明有错误
        if not isinstance(result, dict):
            with open('auido.mp3', 'wb') as f:
                f.write(result)
            playsound('auido.mp3')   #调用cmd并输入命令，打开语音文件;由于WAV文件的打开需要特定的格式，然鹅百度貌似只有mp3格式
    except:
        return "语音合成出现问题 请检查"

    #time.sleep(t)
    #os.system('taskkill /f /im PotPlayerMini64.exe')

def Tuling(t):
    url="http://openapi.tuling123.com/openapi/api/v2"
    data={
	"reqType":0,
    "perception": {
        "inputText": {
            "text": t
        },

    },
    "userInfo": {
        "apiKey": "d96d4b5165a547c8b964767633feca51",
        "userId": "d48bc762e5c5c641"
    }
}
    data=dumps(data)    #将所要发送的数据转换为json格式
    r=post(url,data)
    res=r.json()               #将返回的数据转换为json格式，最终得到字典型的数据
    res=res.get('results', '未返回正确的文本')
    res=str(res)[60:-4]   #将结果剪切只留下文本部分
    #res=dict(res)
    return res









