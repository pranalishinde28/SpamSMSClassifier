#DearPyGUI Imports
from dearpygui.core import *
from dearpygui.simple import *

#SMS Spam Filter Imports
import random
import pandas as pd
import string
import nltk
nltk.download('punkt')
nltk.download('stopwords')

from functions import categorize_words, pre_process, predict

def check_spam(sender, data, pred=[]):
    with window("Simple SMS Spam Filter"):
        if pred == []:
            add_spacing(count=12)
            add_separator()
            add_spacing(count=12)
            input_value = get_value("Input")
            input_value = pre_process(input_value)
            pred_text, text_colour = predict(input_value)


            pred.append(pred_text)
            add_text(pred[-1], color = text_colour)
        else:
        hide_item(pred[-1])
        input_value = get_value("Input")
        input_value = pre_process(input_value)
        pred_text, text_colour = predict(input_value)


        pred.append(pred_text)
        add_text(pred[-1], color = text_colour)

###window settings
set_main_window_size(540, 72)
set_global_font_scale(1.25)
set_theme("Gold")
set_style_window_padding(30,30)

with window("Simple SMS Spam Filter", width = 520, height=677):
    print("GUI is running...")
    set_window_pos("Simple SMS Spam Filter", 0,0)
    add_drawing("logo", width=520,height=290)
    add_separator()
    add_spacing(count = 12)
    add_text("Please enter an SMS of your choice to check if it's spam or not" ,
    color=[232,163,33])
    add_spacing(count = 12)
    add_input_text("Input", width=415, default_value="type message here!")
    add_spacing(count = 12)
    add_button("Check", callback=check_spam)


draw_image("logo", "logo_spamFilter.png", [0,240])


start_dearpygui()
    
