import json


class Message:
    title = None  # title of push notification
    content = None  # content of push notification
    imageURL = None  # image url of push notification
    message = None  # whole data as json

    def __init__(self, title, content, imageURL):
        self.title = title
        self.content = content
        self.imageURL = imageURL
        self.message = json.dumps({"title": title, "content": content, "imageURL": imageURL})
