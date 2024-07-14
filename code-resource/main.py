# Importing the required modules
import tkinter as tk
import tkinter.filedialog as fd
import img2pdf as img

"""
    This is an GUI Application designed in order to convert the images or General Image format to the pdf files.
    Also, below we have the details regarding the modules that we have used in this project.

    Modules Details :
    1. Tkinter : It is general module used for designing the GUI Application in order to form a proper GUI Window.
    2. Tkinter.filedialog : This particular module from Tkinter Library is been used in order to choose a particular file from the Explorer.
    3. img2pdf : It is the main module which is been used for convertion of normal Image into a proper pdf file.

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

# adding label to it
lb1 = tk.Label(w1,text = 'Img2pdf Converter',font = ('Fira Code',10,'bold'),fg = "#F9D342",bg = "#292826")
lb1.pack(padx = 2,pady = 10)

# defining method for Selection of Images
# Selection of Images using filedialog Module method askfilenames

def select():
    global files1                                                               # Specifying File Names variable to be Global
    files1 = fd.askopenfilenames(initialdir = '/',title = 'Select files')

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
            with open(f"file {index}.pdf","wb") as f:                                   # Opening file in binary write format
                f.write(img.convert(file_name))                                         # Rewrite and converting into file

        elif e1.get() == "":
            with open("single.pdf","wb") as f:                                          # Opening file in binary write format
                f.write(img.convert(file_name))                                         # Rewrite and converting into file
        
        else:
            with open("{filename}.pdf".format(filename = e1.get()),"wb") as f:          # Opening file in binary write format
                f.write(img.convert(file_name))                                         # Rewrite and converting into file
                
# defining method for conversion of multiple files into pdf
# In this multiple file will be converted into single pdf file

def convert_multiple():
    if e1.get() == '':
        with open("file.pdf","wb") as f:                    # Opening Single Files in Write binary format
            f.write(img.convert(files1))                    # Converting intot single file

    elif '.' in e1.get():
        with open("file.pdf","wb") as f:                    # Opening Single Files in Write binary format
            f.write(img.convert(files1))                    # Converting intot single file

    else:
        with open("{file}.pdf".format(file = e1.get()),"wb") as f:                      # Opening Single Files in Write binary format
            f.write(img.convert(files1))                                                # Converting intot single file

# initiating Buttons for convertion of image or images
btn2 = tk.Button(frm1,text = 'Convert Image',command = convert_single,bg = "#F9D342",fg = "#292826")              # Button for Single Image Conversion
btn2.pack(side = 'left',padx = 5)

btn3 = tk.Button(frm1,text = 'Convert Images',command = convert_multiple,bg = "#F9D342",fg = "#292826")           # Button for Multiple Images Conversion
btn3.pack(side = 'right',padx = 3)

w1.mainloop()