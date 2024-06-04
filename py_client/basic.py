import requests


endpoint1 = "https://httpbin.org/headers"
endpoint2 = "https://www.httpbin.org/anything"
endpoint3 = "http://127.0.0.1:8000/api/"


get_response = requests.get(endpoint3, params={"q": "python", "page": 2}, json={"number": 123, "text": "Hello World"})
print(get_response.text)