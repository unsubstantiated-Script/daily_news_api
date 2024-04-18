import os

import requests

from send_email import send_email

api_key = os.getenv("API_KEY")
url = f"https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={api_key}"

print(url)

request = requests.get(url)
content = request.json()

body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + "\n" + article["url"] + 2 * "\n"

body = body.encode("utf-8")
send_email(message=body)
