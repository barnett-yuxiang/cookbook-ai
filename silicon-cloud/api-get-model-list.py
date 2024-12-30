import requests

url = "https://api.siliconflow.cn/v1/models"

querystring = {"type": "text", "sub_type": "chat"}

headers = {
    "Authorization": "Bearer <API Key>"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
