import google.generativeai as genai
"""
使用gemini的api
AIzaSyCENo436BSrGaQabHECEvLMRF_qj_MOQJw

pip install -q -U google-generativeai

curl \
-H 'Content-Type: application/json' \
-d '{ "prompt": { "text": "Write a story about a magic backpack"} }' \
"https://generativelanguage.googleapis.com/v1beta3/models/text-bison-001:generateText?key=YOUR_API_KEY"
"""
api_key = 'AIzaSyCENo436BSrGaQabHECEvLMRF_qj_MOQJw'

genai.configure(api_key=api_key)


model = genai.GenerativeModel('gemini-pro')
# 实际测试504错误
response = model.generate_content("What is the meaning of life?")
