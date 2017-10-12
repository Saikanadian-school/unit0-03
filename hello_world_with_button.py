#coding: utf-8

# Created by: Anthony Freeman
# Created on: September 2017
# Created for: ICS3U

import ui

def hello_world_touch_up_inside(sender):
    #print ('Hello, World!')
    view['hello_world_label'].text = ("Hello, World!")

view = ui.load_view()
view.present('sheet')
