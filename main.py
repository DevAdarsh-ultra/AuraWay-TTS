import kivymd
from kivymd.app import MDApp
from kivy.lang import*
from plyer import tts
KV="""
Screen:
    MDBoxLayout:
        orientation:"vertical"
        pos_hint:{"top":1}
        MDTopAppBar:
            title:"AuraWay TTS"
        FloatLayout:
            MDTextField:
                pos_hint:{"center_x":0.5,"center_y":0.9}
                mode:"rectangle"
                size_hint_y:0.15
                size_hint_x:0.8
                hint_text:"Paste the text here"
                id:i
                multiline:True
            MDRaisedButton:
                text:"Speak"
                pos_hint:{"center_x":0.5,"center_y":0.78}    
                on_release:app.spk(1)         
"""
class A(MDApp):
    def build(self): 
       app=Builder.load_string(KV)
       self.inpu=app.ids.i
       self.theme_cls.theme_style="Dark"
       return app
    def spk(self,instance):
        tts.speak(self.inpu.text)
A().run()