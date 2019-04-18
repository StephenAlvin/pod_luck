from kivy.core.window import Window
Window.fullscreen = 0
Window.size = (400, 600)    #Sets window size upon opening app
Window.clearcolor = (1, 1, 1, 1)    #Sets background colour

from kivy.app import App
from kivy.lang import Builder
import requests
from kivy.core.text import LabelBase

LabelBase.register(name="Pacifico",
                   fn_regular="Pacifico.ttf")   #Import Pacifico font

KV = Builder.load_string ("""     
ScreenManager:
    Screen:
        GridLayout:
            cols:3
            orientation: 'horizontal'
            
            GridLayout:
                cols:1
                rows:1
                Label:
                    text: 'Pod 0'
                    font_name: "Pacifico"
                    bold: True
                    color: 128,0,128,1
                    font_size: 17
                    halign: 'center'
                    valign: 'middle'
                    id: btn0
                    
            GridLayout:
                cols:1
                rows:1
                Label:
                    text: 'Pod 1'
                    font_name: "Pacifico"
                    bold: True
                    color: 128,0,128,1
                    font_size: 17
                    halign: 'center'
                    valign: 'middle'
                    id: btn1
                    
            GridLayout:
                cols:1
                Label:
                    text: 'Pod 2'
                    font_name: "Pacifico"
                    bold: True
                    color: 128,0,128,1
                    font_size: 17
                    halign: 'center'
                    valign: 'middle'
                    id: btn2
                    
            GridLayout:
                cols:1
                rows:1
                Label:
                    text: 'Pod 3'
                    font_name: "Pacifico"
                    bold: True
                    color: 128,0,128,1
                    font_size: 17
                    halign: 'center'
                    valign: 'middle'
                    id: btn3
                    
            GridLayout:
                cols:1
                Label:
                    text: 'Pod 4'
                    font_name: "Pacifico"
                    bold: True
                    color: 128,0,128,1
                    font_size: 17
                    halign: 'center'
                    valign: 'middle'
                    id: btn4
                    
            GridLayout:
                cols:1
                rows:1
                Label:
                    text: 'Pod 5'
                    font_name: "Pacifico"
                    bold: True
                    color: 128,0,128,1
                    font_size: 17
                    halign: 'center'
                    valign: 'middle'
                    id: btn5
                    
            GridLayout:
                cols:1
                Button:
                    text: 'UPDATE'
                    font_name: "Pacifico"
                    color: 1,1,1,1
                    font_size: 20
                    background_normal: 'purplenorm.png'
                    background_down: 'greydown.png'
                    on_release: app.get()
                
            GridLayout:
                rows:1
                Image:
                    source: "pod_luck.PNG"

            GridLayout:
                rows:1
                cols:2
                Button:
                    id:btnExit
                    text:"EXIT"
                    font_name: "Pacifico"
                    color: 1,1,1,1
                    font_size: 20
                    background_normal: 'purplenorm.png'
                    background_down: 'greydown.png'
                    on_press: app.stopping()    #Closes the app when user press the "Exit" button
                    
""")

class POD_LUCKApp(App):

    url = 'https://podluck-b3df6.firebaseio.com/.json'
    auth_key = '2BKTZfCSuILkpIRKzDAIWOMkhaC5jIq069Eg4oLS'

    def get(self):
        request = requests.get(self.url + '?auth=' + self.auth_key)    #pulls data from firebase
        dikt = request.json()   #creates the dictionary below
        #print(dikt)
        #dikt = {'r_pi': ['not_occupied', 'not_occupied', 'not_occupied', 'not_occupied', 'not_occupied']}
        pod_list = dikt['r_pi']    #because the value corresponding to the r_pi key is a list, define the value as a list 
        self.root.ids.btn0.text = "Pod 0\n" + str(pod_list[0])
        self.root.ids.btn1.text = "Pod 1\n" + str(pod_list[1])
        self.root.ids.btn2.text = "Pod 2\n" + str(pod_list[2])
        self.root.ids.btn3.text = "Pod 3\n" + str(pod_list[3])
        self.root.ids.btn4.text = "Pod 4\n" + str(pod_list[4])
        self.root.ids.btn5.text = "Pod 5\n" + str(pod_list[5])
        
    def stopping(self):
        App.get_running_app().stop()    #App stops running
        Window.close()  #Closes the whole window

    def build(self):
        return KV

if __name__ == '__main__':
    POD_LUCKApp().run()
