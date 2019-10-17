import json


class Message:
    title = None  # title of push notification
    content = None  # content of push notification
    image_url = None  # image url of push notification
    JsonMessage = None  # whole data as json

    def __init__(self, title, content, image_url):
        self.title = title
        self.content = content
        self.image_url = image_url
        self.JsonMessage = json.dumps({"title": title, "content": content, "image_url": image_url})
