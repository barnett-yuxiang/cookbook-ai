import requests

url = "https://api.siliconflow.cn/v1/chat/completions"

payload = {
    "model": "Qwen/QVQ-72B-Preview",
    "messages": [
        {
            "role": "user",
            "content": []
        }
    ],
    "stream": False,
    "max_tokens": 4096,
    "temperature": 0.7,
    "response_format": {"type": "text"},
    "n": 1,
    "frequency_penalty": 0.5,
    "top_k": 50,
    "top_p": 0.7
}
headers = {
    "Authorization": "Bearer <API Key>",
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)
