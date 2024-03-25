一、环境 t2iadapter2 用fastchat启动语言模型chatglm2
1.python -m fastchat.serve.controller --host 0.0.0.0
2.CUDA_VISIBLE_DEVICES=1 python -m fastchat.serve.model_worker --model-path ./chatglm-6b/
3.python -m fastchat.serve.openai_api_server --host 0.0.0.0 --port 8001  

这样就启动了llm openai接口在8001


二、tts 启动用docker 启动emotionvoice

三、py39环境下 python test_gradio_tts.py
