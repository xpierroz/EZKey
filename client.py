"""
THIS IS STILL IN DEVELOPMENT BUT IF U WANNA USE JUST PUT YOUR INT IN THE ENCODED STRING AND RUN THE PROGRAM BABYYYYY
"""
"""
15/05/2023 THIS IS STILL NOT WORKING U CAN TRYNA RUN IT BUT IT WILL NOT WORK
"""

from flaskwebgui import FlaskUI
from nicegui import ui, events

import random
import os

__title__ = "EZKey - made by xpierroz"

ui.colors(primary='#333')

def convert_text(text):
    string = ""
    for _encoded_int in text.split("\r\n"):
        for encoded_int in _encoded_int.split(" "):
            if encoded_int == "":
                continue
            
            decoded_bytes = int(str(encoded_int)).to_bytes((int(encoded_int).bit_length() + 7) // 8, byteorder='big')
            decoded_string = decoded_bytes.decode()

            string += f" {decoded_string} "
    return string

def _home():
    ui.label("will be released soon stay patient lol")
    ui.label(".gg/BptVd57QHr")
    
def _translate(text):
    random_number = random.randint(0, 100000)
    name = f"translated_{random_number}.txt"
    with open(name, "w") as f:
        f.write(text)
        
    return name
        
def translate(text):
    name = _translate(text)
    os.startfile(name)
    
def _decoder():
    ui.label("Open your .cache file")
    with ui.dialog().props('full-width') as dialog:
        with ui.card():
            content = ui.markdown()

    def handle_upload(e: events.UploadEventArguments):
        text = e.content.read().decode('utf-8')
        _converted = convert_text(text)
        content.set_content(_converted)
        translate(_converted)
        
    ui.upload(on_upload=handle_upload, multiple=False, auto_upload=True).props('accept=.cache').classes('max-w-full')

with ui.tabs().classes('w-full center') as tabs:
    ui.tab('Home', icon='home')
    ui.tab('Decoder', icon='lock_open')

with ui.tab_panels(tabs, value='Home').classes('bg-transparent').classes('w-full center'):
    with ui.tab_panel('Home'):
        _home()
    with ui.tab_panel('Decoder'):
        _decoder()
            
def start_nicegui(**kwargs):
    ui.run(
        title=__title__,
        **kwargs
    )

if __name__ in {"__main__", "__mp_main__"}:
    DEBUG = False

    if DEBUG:
        ui.run()
    else:
        FlaskUI(
            server=start_nicegui,
            server_kwargs={"dark": True, "reload": False, "show": False, "port": 3000},
            width=500,
            height=650, 
        ).run()




















encoded = """

"""
s = encoded.split("\n")
for _encoded_int in s:
    for encoded_int in _encoded_int.split(" "):
        if encoded_int == "":
            continue
        # Decode the integer to bytes object
        decoded_bytes = int(encoded_int).to_bytes((int(encoded_int).bit_length() + 7) // 8, byteorder='big')

        # Decode the bytes object to a string
        decoded_string = decoded_bytes.decode()

        # Print the decoded string
        print(decoded_string)