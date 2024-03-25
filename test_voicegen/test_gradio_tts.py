import gradio as gr
from TTS.api import TTS
import librosa
import os 
title = "文本转语音"

""""文本转语音的demo,加入llms-chat对话后改造成了输入文本语音输出
例如 输入文本：你是谁
    输出一段语音：我是人工智能助手....
"""
def generateAudio(text):
    #由于TTS无法很好地处理回车符和空格，需要对text里的回车符进行替换
    text = text.replace("\n",",")
    text = text.replace(" ","")
    tts = TTS(model_name="tts_models/zh-CN/baker/tacotron2-DDC-GST", progress_bar=True, gpu=False)
    tts.tts_to_file(text,file_path="output.wav") 
    
    audio, sr = librosa.load(path="output.wav")
    
    return  sr,audio


def generate(text):
    import requests

    url = 'https://example.com/api'
    data = {'key1': 'value1', 'key2': 'value2'}
    url ="http://10.250.115.90:8000/v1/audio/speech"
    
    ret = get_completion(text)

    data = {
      "input": ret,
      "voice": "8051",
      "prompt": "开心",
      "language": "zh_us",
      "model": "emoti-voice",
      "response_format": "mp3",
      "speed": 1
    }

    # response = requests.post(url, data=data)
    headers = {'content-type': 'application/json'}
    ret = requests.post(url, json=data, headers=headers, timeout=10)
    print(ret)
    # print(response.status_code)
    # print(response.content)
    # print(ret.content)
    f = open("333.mp3", "wb")
    f.write(ret.content)
    f.close()
    audio, sr = librosa.load(path="333.mp3")
    
    return  sr,audio

import os
import openai
 
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
os.environ['OPENAI_API_KEY'] = 'EMPTY'
os.environ['OPENAI_API_BASE'] = 'http://localhost:8001/v1'
openai.api_key = 'none'
openai.api_base = 'http://localhost:8001/v1'

def get_completion(prompt, model="chatglm-6b"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]

# print(get_completion("你是谁?"))

app = gr.Interface(
    fn=generate, 
    inputs="text", 
    outputs="audio", 
    title=title,
    examples=[os.path.join(os.path.dirname(__file__),"output.wav")]
    )

app.launch(server_name="0.0.0.0",ssl_verify=False, ssl_certfile="./cert.pem", ssl_keyfile="./key.pem")

