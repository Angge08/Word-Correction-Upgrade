import PySimpleGUI as sg
from textblob import TextBlob, Word
import pyttsx3

engine = pyttsx3.init()
sg.theme('LightGreen6')
sg.set_options(font='Verdana 15')

layout = [  [sg.Text('Input Word'),sg.Input(key='-IN-')],
            [sg.Button('Corrected Word'), sg.Button('Speak'), sg.Button('Clear'), sg.Button('Exit',expand_y=True)],
            [sg.Multiline(disabled=True, key='-OUT-', size=(100,20))]
        ]
window = sg.Window('Word Correction', layout)
def clear_inputs():
    for key in values:
        window['-IN-'].update('')