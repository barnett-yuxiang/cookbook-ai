from openai import OpenAI

client = OpenAI(
    base_url='https://<hidden>.api-inference.modelscope.cn/v1',
    api_key='<hidden>', # ModelScope Token
)

response = client.chat.completions.create(
    model='Qwen/QwQ-32B-GGUF', # ModelScope Model-Id
    messages=[
        {
            'role': 'system',
            'content': 'You are a helpful assistant.'
        },
        {
            'role': 'user',
            'content': 'Hello, how are you?'
        }
    ],
    stream=True
)

for chunk in response:
    print(chunk.choices[0].delta.content, end='', flush=True)
