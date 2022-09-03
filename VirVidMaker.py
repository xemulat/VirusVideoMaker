import PySimpleGUI as sg
from time import sleep
from os import system, remove
from sys import exit
from urllib.request import urlretrieve

system('cls')
sg.theme("DarkGray15")
sg.set_options(font=("Consolas", 9), text_color='#FFFFFF')
urlretrieve('https://raw.githubusercontent.com/xemulat/VirusVideoMaker/main/texttofile.txt', 'fake-tmp.txt')
with open("fake-tmp.txt","r") as FileX:
    fpload = FileX.read()

def done():
    custom = [[sg.Text('Fake Virus has been injected')],
              [sg.Text('Click "X" to close!')],
              [sg.Text('')],
              [sg.Text('Coded by Xemulated')]]

    window = sg.Window('VirVidMaker', custom)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            remove('fake-tmp.txt')
            exit()

def injects(fname):
    file1 = open(fname, "a")  # adds some fake malware text lul
    file1.write('\n')
    file1.write(fpload)
    file1.close()
    done()

def getdata():
    custom = [[sg.Text('Filename of the video to inject the "virus":')],
              [sg.Text('Press Enter to confirm')],
              [sg.Input('', enable_events=True,  key='-INPUT-', )],
              [sg.Button('Exit')],
              [sg.Button('Enter', visible=True, bind_return_key=True)],
              [sg.Text('')],
              [sg.Text('Coded by Xemulated')]]

    window = sg.Window('VirVidMaker', custom)

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            exit()
        
        elif event == 'Enter':
            window.close()
            injects(window['-INPUT-'].get())
getdata()
