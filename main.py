import gradio as gr
# from openai import OpenAI
import openai
from pathlib import Path

# 配置你的apikey ，如果在国内可能还需要配置openai接口镜像地址
# client = OpenAI(
#     api_key='',
#     base_url=''
# 

"""语音识别->llms chat -> TTS语音输出 都是通过调用openai 的接口实现"""

def transcribe_audio(audio_file_path):
    with open(audio_file_path, "rb") as audio_file:
        transcribed_text =  client.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file, 
        response_format="text"
    )
    # 使用 GPT-3.5 处理转录的文本
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": transcribed_text}
        ]
    )
    gpt_response = response.choices[0].message.content

    speech_response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=gpt_response
    )
    speech_file_path = Path("speech.mp3")
    speech_response.stream_to_file(speech_file_path)

    return transcribed_text, gpt_response,speech_file_path

# 创建 Gradio 界面
with gr.Blocks() as demo:
    with gr.Row():
        audio_input = gr.Audio(type="filepath", label="录音")
        
    with gr.Row():
        transcribed_text = gr.Textbox(label="转录文本")
        gpt_response_output = gr.Textbox(label="GPT-3.5 回应")
        speech_file_path = gr.Audio(label="播放语音回应", type="filepath")

    gr.Button("转录").click(
        fn=transcribe_audio, 
        inputs=audio_input, 
         outputs=[transcribed_text, gpt_response_output, speech_file_path]
    )

demo.launch(server_name="0.0.0.0",ssl_verify=False, ssl_certfile="./cert.pem", ssl_keyfile="./key.pem")
# demo.launch(server_name="0.0.0.0")
