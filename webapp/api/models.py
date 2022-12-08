from django.db import models

# Create your models here.
class HTMLtext:
    def __init__(self, url, text):
        self.url = url
        self.text = text