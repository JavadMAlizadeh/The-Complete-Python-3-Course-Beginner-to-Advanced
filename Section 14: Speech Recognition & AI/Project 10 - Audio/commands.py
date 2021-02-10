import subprocess
import os
import requests
from bs4 import BeautifulSoup
import pyttsx3
from Section_14.get_answer import Fetcher


class Commander:
    def __init__(self):
        self.exit = ["quit", "goodbye", "exit", "bye"]
        self.confirm = ["yes", "affirmative", "si", "sure", "do it", "yeah", "confirm"]
        self.cancel = ["no", "negative", "negative soldier", "don't", "wait", "cancel"]

    def discover(self, text):
        if "what" in text and "name" in text:
            if "my" in text:
                self.respond("You haven't told me your name yet!")
            else:
                self.respond("My name is Python commander. How are you?")
        else:
            f = Fetcher("https://www.google.com/search?q=" + text)
            answer = f.lookup()
            self.respond(answer)

    def respond(self, response):
        newfile = open("test.txt", "w+")
        newfile.write(response)
        newfile.flush()
        engine = pyttsx3.init()
        engine.say(response)
        engine.runAndWait()


