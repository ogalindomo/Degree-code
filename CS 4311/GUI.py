from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.graphics import Color, Rectangle
from random import random as r
from functools import partial
from kivy.core.window import Window

    
class Demo(Widget):
        #######nitialize main Window#######

#        self.clearcolor = (0.5,0,0.1,1)x1
#        self.background_normal = ''
#        self.background_color = (1,1,1,1)
#        self.clear_color(1,1,1,1)
        ###################################
        app_interface = Widget()    
        with app_interface.canvas:
            Color(1,1,1,1)
            Rectangle(pos=app_interface.center, size=(app_interface.width/2., app_interface.height/2.))
#        app_interface.canvas = Color(1,1,1,1)
        stopapp = partial(stop)
        stop_button = Button(text='stop', background_color = (0.8,0.2,0.05,1), background_normal = '')
        stop_button.bind(on_press = stopapp)
        
        ###################################
        label = Label()
        
        layout = BoxLayout(size_hint=(1,None), height=50)
        
        layout.add_widget(label, index = 3)
        layout.add_widget(stop_button)
        
        root = BoxLayout(orientation='horizontal')
        root.add_widget(app_interface)
        root.add_widget(layout)
#        return self
    
class GUI(App):
    def build(self):
        self.title = "Network Traffic Proxy System"
        self.size = (750,750)
        stop_all = partial(App.get_running_app().stop)
        self.bind(on_close = stop_all)
        return Demo()

if __name__ == '__main__':
    GUI().run()

#class StressCanvasApp(App):
#
#    def add_rects(self, label, wid, count, *largs):
#        label.text = str(int(label.text) + count)
#        with wid.canvas:
#            for x in range(count):
#                Color(r(), 1, 1, mode='hsv')
#                Rectangle(pos=(r() * wid.width + wid.x,
#                               r() * wid.height + wid.y), size=(20, 20))
#
#    def double_rects(self, label, wid, *largs):
#        count = int(label.text)
#        self.add_rects(label, wid, count, *largs)
#
#    def reset_rects(self, label, wid, *largs):
#        label.text = '0'
#        wid.canvas.clear()
#
#    def build(self):
#        wid = Widget()
#
#        label = Label(text='0')
#
#        btn_add100 = Button(text='+ 100 rects',
#                            on_press=partial(self.add_rects, label, wid, 100))
#
#        btn_add500 = Button(text='+ 500 rects',
#                            on_press=partial(self.add_rects, label, wid, 500))
#
#        btn_double = Button(text='x 2',
#                            on_press=partial(self.double_rects, label, wid))
#
#        btn_reset = Button(text='Reset',
#                           on_press=partial(self.reset_rects, label, wid))
#
#        layout = BoxLayout(size_hint=(1, None), height=50)
#        layout.add_widget(btn_add100)
#        layout.add_widget(btn_add500)
#        layout.add_widget(btn_double)
#        layout.add_widget(btn_reset)
#        layout.add_widget(label)
#
#        root = BoxLayout(orientation='vertical')
#        root.add_widget(wid)
#        root.add_widget(layout)
#
#        return root
#
#
#if __name__ == '__main__':
#    StressCanvasApp().run()