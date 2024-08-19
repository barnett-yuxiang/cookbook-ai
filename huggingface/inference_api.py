# Running Inference with API Requests
# https://huggingface.co/docs/api-inference/quicktour

import requests

API_URL = "https://api-inference.huggingface.co/models/gpt2"
API_TOKEN = "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"

def query(prompt):
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_length": 100,  # 生成文本的最大长度
            "num_return_sequences": 1  # 返回几条结果
        }
    }
    response = requests.post(API_URL, headers=headers, json=payload)

    # Inspect the response status and content
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)

    return response.json()

data = query("Can you please let us know more details about your ")

# Output:
# Status Code: 200
# Response Text: [{"generated_text":"Can you please let us know more details about your iphone?\n\n
# We are currently working on a new app for iPhone and iPad.
# We are working on a new app for iPhone and iPad.
# We are working on a new app for iPhone and iPad. We are working on a new app for iPhone and iPad.
# We are working on a new app for iPhone and iPad. We are working on a new app for iPhone and iPad.
# We are working on a new app for iPhone and iPad. We are working on a new app for iPhone and"}]
