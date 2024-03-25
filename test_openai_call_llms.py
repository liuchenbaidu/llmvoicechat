import os
import openai
 """"用fastchat部署chatglm6b为openai的api接口后，用openai库调用"""
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

print(get_completion("你是谁?"))
