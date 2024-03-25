import gradio as gr

with gr.Blocks() as demo:
    # gr.Audio(value="nihao.mp3",type="filepath")
    audio_input = gr.Audio(type="filepath", label="录音")

# demo.launch(server_name="0.0.0.0",server_port=16667)
demo.launch(server_name="0.0.0.0",ssl_verify=False, ssl_certfile="./cert.pem", ssl_keyfile="./key.pem")
