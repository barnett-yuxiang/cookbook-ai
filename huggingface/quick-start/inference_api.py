# Running Inference with API Requests
# https://huggingface.co/docs/api-inference/quicktour

# Test gpt2
import requests

API_URL = "https://api-inference.huggingface.co/models/gpt2"
API_TOKEN = "<Your Token>"

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


# Test pegasus
import requests

API_URL = "https://api-inference.huggingface.co/models/google/pegasus-xsum"
headers = {"Authorization": "Bearer hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

output = query({
    "inputs": "The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris. Its base is square, measuring 125 metres (410 ft) on each side. During its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest man-made structure in the world, a title it held for 41 years until the Chrysler Building in New York City was finished in 1930. It was the first structure to reach a height of 300 metres. Due to the addition of a broadcasting aerial at the top of the tower in 1957, it is now taller than the Chrysler Building by 5.2 metres (17 ft). Excluding transmitters, the Eiffel Tower is the second tallest free-standing structure in France after the Millau Viaduct.",
})
print(output)

# Output:
# [{'summary_text': 'The Eiffel Tower is a landmark in Paris, France.'}]
