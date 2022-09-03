import PySimpleGUI as sg
from os import remove
from sys import exit
from urllib.request import urlretrieve
from lastversion import latest
from ping3 import ping
from os.path import isfile

# ===============< Prep Phase >===============
if isfile('samplevideo.mp4') == True:
    remove('samplevideo.mp4')
sg.theme("DarkGray15")
sg.set_options(font=("Consolas", 9), text_color='#FFFFFF')
urlretrieve('https://raw.githubusercontent.com/xemulat/VirusVideoMaker/main/texttofile.txt', 'temp.vvgen')
with open("temp.vvgen","r") as FileX:
    fpload = FileX.read()

# ===============< The Injector >===============
def injects(fname):
    file1 = open(fname, "a")
    file1.write('\n')
    file1.write(fpload)
    file1.close()
    done()

# ===============< Done Popup >===============
def done():
    custom = [[sg.Text('Fake Virus has been injected')],
              [sg.Text('Click "X" to close!')],
              [sg.Text('')],
              [sg.Text('Coded by Xemulated')]]

    window = sg.Window('VirVidMaker', custom)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            remove('temp.vvgen')
            exit()

def getdata():
    # ===============< Updater >===============
    newver = latest('xemulat/VirusVideoMaker')
    if "1.1" == str(newver):
        vers = "Your Version is Up-To-Date!"
    elif str(newver) > "1.1":
        vers = "Your Version is Outdated, download it from My repo!"
    else:
        vers = "Unable to check updates :("
    # ===============< Internet Chacker >===============
    internet = ping("https://www.github.com/")
    if internet == None or False:
        internetac = "Network Unreachable"
    else:
        internetac = "Network Reachable"
    # ===============< Main Window >===============
    custom = [[sg.Text("Status: \n" + vers + "\n" + internetac)],
              [sg.Text("")],
              [sg.Text('Filename of the video to inject the "virus":')],
              [sg.Text('Press Enter to confirm')],
              [sg.Input('', enable_events=True,  key='-INPUT-', )],
              [sg.Button('Exit'), sg.Button('Enter', visible=True, bind_return_key=True), sg.Button('Sample Video')],
              [sg.Text('')],
              [sg.Text('Coded by Xemulated')]]

    window = sg.Window('VirVidMaker', custom)

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            remove('temp.vvgen')
            exit()
        
        if event == 'Sample Video':
            urlretrieve("https://github.com/xemulat/VirusVideoMaker/raw/main/cinder.mp4", "samplevideo.mp4")
            window.close()
            injects("samplevideo.mp4")

        elif event == 'Enter':
            if window['-INPUT-'].get() == '':
                pass
            else:
                window.close()
                injects(window['-INPUT-'].get())
getdata()
