import os

import requests

from send_email import send_email

topic = "top-headlines"
api_key = os.getenv("API_KEY")
url = (f"https://newsapi.org/v2/{topic}?"
       f"sources=techcrunch&"
       f"apiKey={api_key}&"
       f"language=en")

print(url)

request = requests.get(url)
content = request.json()

body = "Subject: Today's News" + "\n"
# This lists up to 20 articles.
for article in content["articles"][:20]:
    if (article["description"] is not None) and (article["title"] is not None):
        body = (body + article["title"] + "\n"
                + article["description"] + "\n"
                + article["url"] + 2 * "\n")

body = body.encode("utf-8")
send_email(message=body)
