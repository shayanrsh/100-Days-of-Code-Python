import requests


class Post:
    def __init__(self):
        self.url = "https://api.npoint.io/c790b4d5cab58020d391"
        response = requests.get(self.url)
        response.raise_for_status()
        posts = response.json()
        self.titles = [post["title"] for post in posts]
        self.subtitles = [post["subtitle"] for post in posts]
        self.bodies = [post["body"] for post in posts]