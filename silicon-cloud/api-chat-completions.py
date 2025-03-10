import requests

url = "https://api.siliconflow.cn/v1/chat/completions"

payload = {
    "model": "Qwen/QVQ-72B-Preview",
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://sf-maas-uat-prod.oss-cn-shanghai.aliyuncs.com/outputs/658c7434-ec12-49cc-90e6-fe22ccccaf62_00001_.png",
                        "detail":"high"
                    }
                },
                {
                    "type": "text",
                    "text": "Please describe the content of the picture, the more detailed the better"
                }
            ]
        }
    ],
    "stream": False,
    "max_tokens": 4096,
    "temperature": 0.2,
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
