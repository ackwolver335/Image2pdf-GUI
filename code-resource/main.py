# Importing the required modules
import tkinter as tk
import tkinter.filedialog as fd
import img2pdf as img
import tkinter.messagebox as mg
import os
import shutil

"""
    This is an GUI Application designed in order to convert the images or General Image format to the pdf files.
    Also, below we have the details regarding the modules that we have used in this project.

    Modules Details :
    1. Tkinter : It is general module used for designing the GUI Application in order to form a proper GUI Window.
    2. Tkinter.filedialog : This particular module from Tkinter Library is been used in order to choose a particular file from the Explorer.
    3. img2pdf : It is the main module which is been used for convertion of normal Image into a proper pdf file.
    4. tkinter.messagebox : It is used for providing messagebox alert or warning regarding user unusual behaviour.
    5. os : It is used for getting current location of the folder.
    6. shutil : It is used for getting file moved from one location to another.

    Further Details regarding the Methods used in these Modules :

    - Tkinter : General Module for GUI Integration.
    
    >> Methods Used :
    1. Tk() : Used for Initiating GUI Window.
    2. title() : Used for giving title to the GUI Window.
    3. resizable() : Used for defining whether the window needs to be defined or not.
    4. config() : General method used for changing configuration of different Widgets.
    5. Label() : It is used for creating Label Widget.
    6. pack() : Used for management placement of GUI Widgets.
    7. Frame() : It is used for creating frames inside the GUI Window.
    8. Button() : Used for creating Button Widgets in GUI Interface.
    9. Entry() : Used for adding entry label to the Window.
    10. mainloop() : Used for looping the window until it is been manually closed by the user.

    - tkinter.filedialog : Module available inside tkinter library for getting work regarding files

    >> Methods Used :
    1. askopenfilenames() : It is used for asking data regarding which file is to be opened.

    - img2pdf : Module used for converting either single or multiple images into a pdf file.

    >> Methods Used :
    1. convert() : It is used for converting the given image files into a proper pdf file.

"""

# defining the window and its further components regarding GUI window Developement or Design
# main window
w1 = tk.Tk()

w1.title('Image To PDF Converter')                      # Window's Title
w1.geometry('300x190')                                  # Window's Dimension
w1.resizable(False,False)                               # Unabling the Window to get Resizable
w1.config(background = "#292826")                       # setting up background color

# A general information and warning to the user
mg.showinfo('Application Information','You must need to give the name of file and location before converting and after conversion only you have the choice to move the file Otherwise you may get an error !')

# adding label to it
lb1 = tk.Label(w1,text = 'Img2pdf Converter',font = ('Fira Code',10,'bold'),fg = "#F9D342",bg = "#292826")
lb1.pack(padx = 2,pady = 10)

# defining method for Selection of Images
# Selection of Images using filedialog Module method askfilenames

def select():
    global files1                                                               # Specifying File Names variable to be Global
    files1 = fd.askopenfilenames()

# defining a function or method for selecting file's location
def select_location():
    global file_location
    file_location = fd.askdirectory()

# defining move method for moving the file location to the directory that user wants
def move_file():
    if e1.get() == '' or file_location == '':
        mg.showwarning('Application Error','Either the file is not renamed or Location is not selected !')
    else:
        new_location = file_location + "\\" + e1.get() + ".pdf"
        current_dir = os.getcwd()  + "\\" + e1.get() + ".pdf"
        shutil.move(current_dir,new_location)

# adding some Button for the main purpose
btn1 = tk.Button(w1,text = 'Select Image/Images',command = select,bg = "#F9D342",fg = "#292826")
btn1.pack(padx = 2,pady = 5)

# Specify a Frame for Overall Data
frm1 = tk.Frame(w1,bg = "#292826")
frm1.pack(padx = 2,pady = 3)

# Providing title for Entry Widget
# Label inside the main frame
lb2 = tk.Label(frm1,text = 'Rename File',fg = "#F9D342",bg = '#292826',font = ('Fira Code',10,'bold'))
lb2.pack(padx = 2,pady = 3)

# defining an entry for getting the name of file that user wants to set
# Entry for file name
e1 = tk.Entry(frm1)
e1.pack(padx = 2,pady = 10)

# defining method for conversion of single image
# here we will use bit format of file and reading the file before its conversion

def convert_single():
    for index, file_name in enumerate(files1):                                      # Specifying index for first image and its names
        
        # Specifying cases for file name if user try to attach extension
        if '.' in e1.get():
            mg.showwarning('Application Warning','Do not use . while giving file name !')                                           # message warning to the user

        elif e1.get() == "" or file_location == '':
            mg.showwarning('Application Warning','Please fill out the name of pdf file or select file location !')                  # message warning to the user
        
        else:
            with open("{filename}.pdf".format(filename = e1.get()),"wb") as f:          # Opening file in binary write format
                f.write(img.convert(file_name))                                         # Rewrite and converting into file
                
# defining method for conversion of multiple files into pdf
# In this multiple file will be converted into single pdf file

def convert_multiple():
    if e1.get() == '' or file_location == '':
        mg.showwarning('Application Warning','Please fill out the name of pdf file or select file location !')

    elif '.' in e1.get():
        mg.showwarning('Application Warning','Do not use . while giving file name !')

    else:
        with open("{file}.pdf".format(file = e1.get()),"wb") as f:                      # Opening Single Files in Write binary format
            f.write(img.convert(files1))                                                # Converting intot single file

# button for selecting location as per user preferrence
btn4 = tk.Button(frm1,text = 'Select Location',bg = "#F9D342",fg = "#292826",command = select_location)
btn4.pack(padx = 3,pady = 3)

# initiating Buttons for convertion of image or images
btn2 = tk.Button(frm1,text = 'Convert Image',command = convert_single,bg = "#F9D342",fg = "#292826")              # Button for Single Image Conversion
btn2.pack(side = 'left',padx = 5)

btn3 = tk.Button(frm1,text = 'Convert Images',command = convert_multiple,bg = "#F9D342",fg = "#292826")           # Button for Multiple Images Conversion
btn3.pack(side = 'right',padx = 3)

# adding button to move files using methods
btn5 = tk.Button(w1,text = 'Move File',command = move_file,bg = "#F9D342",fg = "#292826")
btn5.pack(padx = 3,pady = 3)

w1.mainloop()