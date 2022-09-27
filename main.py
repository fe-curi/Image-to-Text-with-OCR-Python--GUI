from distutils import text_file
import tkinter as tk
from PySimpleGUI.PySimpleGUI import Exit
import easyocr
import PySimpleGUI as sg
import os.path
from fpdf import FPDF


sg.theme('dark2')

file_list_column = [

    [

        sg.Text("Image Folder"),

        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),

        sg.FolderBrowse(),

    ],

    [

        sg.Listbox(

            values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"

        )

    ],

]

 

image_viewer_column = [

    [sg.Text("Choose an image from list on left:")],

    [sg.Text(size=(60, 1), key="-TOUT-")],

    [sg.Image(key="-IMAGE-")],

]


transform_image_column = [

          [sg.Text("Press Transform Button for Convert")],

          [sg.Text(size=(50,1),key='-TRANSFORM-')],

          [sg.Button('Transform')],

          [sg.Text("------------------------------------------------------------------")],

          [sg.Text("Convert to PDF")],

          [sg.Text(size=(50,1),key='-CONVERT-')],

          [sg.Button('Convert')],

]


layout = [

    [

        sg.Column(file_list_column),

        sg.VSeperator(),

        sg.Column(image_viewer_column),

        sg.VSeparator(),

        sg.Column(transform_image_column),

    ]

]


window = sg.Window("Image to Text", layout)





while True:

    event, values = window.read()


    if event == "Exit" or event == sg.WIN_CLOSED:
        break


    if event == 'Transform':
        reader = easyocr.Reader(['en', 'tr'])
        results = reader.readtext(filename)
        print(results)
        text = ''
        for result in results :
            text += result[1] + ' '
        f = open("////Dosya konumu girin", "w+")
        f.write(text)
        print(text)


    if event == 'Convert':
        fpdf = FPDF('P','mm','Letter')
        fpdf.add_page()
        fpdf.set_font('helvetica',size = 12)
        text = open("///Dosya konumu girin", "r")
        for line in text:       
            fpdf.multi_cell(w= 0, h= 10, txt= line, border = 0, 
                align= 'J', fill= False)
        fpdf.output(r"///Dosya konumu girin")


    if event == "-FOLDER-":

        folder = values["-FOLDER-"]

        try:      

            file_list = os.listdir(folder)

        except:

            file_list = []


        fnames = [

            f

            for f in file_list

            if os.path.isfile(os.path.join(folder, f))

            and f.lower().endswith((".png",".gif",".jpg",".jpeg"))

        ]

        window["-FILE LIST-"].update(fnames)

    elif event == "-FILE LIST-":  

        try:

            filename = os.path.join(

                values["-FOLDER-"], values["-FILE LIST-"][0]

            )
            print(filename) 

            window["-TOUT-"].update(filename)

            window["-IMAGE-"].update(filename=filename)

        except:
            pass

window.close()



