import PySimpleGUI as sg
from os import remove
from sys import exit
from urllib.request import urlretrieve
from lastversion import latest
from ping3 import ping
from os.path import isfile
from json import load
# QuickInstall - pip install ping3 lastversion PySimpleGUI

# ===============< Prep Phase >===============
sg.theme("DarkGray15")
sg.set_options(font=("Consolas", 9), text_color='#FFFFFF')
if isfile("settings.vvgen") == False:
    urlretrieve('https://raw.githubusercontent.com/xemulat/VirusVideoMaker/main/settings.vvgen', 'settings.vvgen')
urlretrieve('https://raw.githubusercontent.com/xemulat/VirusVideoMaker/main/texttofile.txt', 'temp.vvgen')
with open("temp.vvgen", "r") as FileX:
    fpload = FileX.read()

# ===============< The Injector >===============
def injects(fname):
    file1 = open(fname, "a")
    file1.write('\n')
    file1.write(fpload)
    file1.close()
    remove('temp.vvgen')
    popup = [[sg.Text('Fake virus successfully injected!', text_color="#27FF00")],
             [sg.Text('Auto-Close in 3s')],
             [sg.Text('')],
             [sg.Text('Coded by Xemulated')]]
    window = sg.Window('VVGen', popup)
    while True:
        event, values = window.Read(timeout=3000)  # in milliseconds
        if event == (sg.WIN_CLOSED) or ('__TIMEOUT__',):
            exit()

def getdata():
    # ===============< Updater & Settings Check >===============
    with open('settings.vvgen') as f:
        d = load(f)
        if str(d["EnableDev"]) == "True":
            newver = "dev"
        else:
            newver = latest('xemulat/VirusVideoMaker')
        if "1.3" == str(newver):
            vers = "Up-To-Date"
            hcve = "#00FF00"
        elif str(newver) == "dev":
            vers = "Dev build, not checking for updates"
            hcve = "#74D962"
        elif str(newver) > "1.3":
            vers = "Outdated, download it from my github"
            hcve = "#FF0000"
        else:
            vers = "error checking updates :("
            hcve = "#FFFF00"
        print("Build: " + str(newver))

    # ===============< Internet Chacker >===============
    internet = ping("https://www.github.com/")
    if internet is None or False:
        internetac = "Unreachable"
        hcin = "#FF0000"
    else:
        internetac = "Reachable"
        hcin = "#00FF00"

    # ===============< Main Window >===============
    custom = [[sg.Text("Version - " + vers, text_color=hcve)],
              [sg.Text("Network - " + internetac, text_color=hcin)],
              [sg.Text("")],
              [sg.Text('Filename of the video to inject the "virus":')],
              [sg.Text('Press Enter to confirm')],
              [sg.Input('', enable_events=True, key='-INPUT-', ), sg.Button('Enter', visible=True, bind_return_key=True)],
              [sg.Button('Sample Video'), sg.Button('Exit')],
              [sg.Text('')],
              [sg.Text('Coded by Xemulated')]]

    window = sg.Window('VirVidMaker', custom)

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            remove('temp.vvgen')
            exit()

        elif event == 'Sample Video':
            if isfile('samplevideo.mp4') == True:
                remove('samplevideo.mp4')
            urlretrieve(
                "https://github.com/xemulat/VirusVideoMaker/raw/main/cinder.mp4", "samplevideo.mp4")
            window.close()
            injects("samplevideo.mp4")

        elif event == 'Enter':
            if window['-INPUT-'].get() == '':
                pass
            elif isfile(window['-INPUT-'].get()) == False:
                pass
            else:
                window.close()
                injects(window['-INPUT-'].get())
getdata()
