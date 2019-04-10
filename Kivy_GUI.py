from kivy.core.window import Window
Window.fullscreen = 0
Window.size = (1000, 500)
from kivy.app import App
from kivy.lang import Builder
import json
import requests
from kivy.properties import ObjectProperty


KV = Builder.load_string ("""     

ScreenManager:
    Screen:
        GridLayout:
            cols:3
            orientation: 'horizontal'
            GridLayout:
                cols:1
                Label:
                    text: 'Pod 0'
                    id: btn0
            GridLayout:
                cols:1
                Label:
                    text: 'Pod 1'
                    id: btn1
            GridLayout:
                cols:1
                Label:
                    text: 'Pod 2'
                    id: btn2
            GridLayout:
                cols:1
                Label:
                    text: 'Pod 3'
                    id: btn3
            GridLayout:
                cols:1
                Label:
                    text: 'Pod 4'
                    id: btn4
            GridLayout:
                cols:1
                Label:
                    text: 'Pod 5'
                    id: btn5
                    
            GridLayout:
                cols:1
                Label:
                
            GridLayout:
                rows:1
                Button:
                    text: 'UPDATE'
                    font_size: 70
                    on_release: app.get()
                    
""")

class MyApp(App):

    url = 'https://podluck-b3df6.firebaseio.com/.json'
    auth_key = '2BKTZfCSuILkpIRKzDAIWOMkhaC5jIq069Eg4oLS'

    def get(self):
        request = requests.get(self.url + '?auth=' + self.auth_key)  #pulls data from firebase
        dikt = request.json() #creates the dictionary below
        #dikt = {'r_pi': ['not_occupied', 'not_occupied', 'not_occupied', 'not_occupied', 'not_occupied']}
        pod_list = dikt['r_pi'] #because the value corresponding to the r_pi key is a list, define the value as a list 
        self.root.ids.btn0.text = "Pod 0 is " + str(pod_list[0]) + "."
        self.root.ids.btn1.text = "Pod 1 is " + str(pod_list[1]) + "."
        self.root.ids.btn2.text = "Pod 2 is " + str(pod_list[2]) + "."
        self.root.ids.btn3.text = "Pod 3 is " + str(pod_list[3]) + "."
        self.root.ids.btn4.text = "Pod 4 is " + str(pod_list[4]) + "."
        self.root.ids.btn5.text = "Pod 5 is " + str(pod_list[5]) + "."

    def build(self):
        return KV

if __name__ == '__main__':
    MyApp().run()
