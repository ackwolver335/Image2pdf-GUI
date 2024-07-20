import tkinter as tk
import tkinter.filedialog as fd
import img2pdf as img
import tkinter.messagebox as mg
import os
import shutil

w1 = tk.Tk()

w1.title('Image To PDF Converter')
w1.geometry('300x250')                
w1.resizable(False,False)                               
w1.config(background = "#292826")           

mg.showinfo('Application Information','You must need to give the name of file and location before converting and after conversion only you have the choice to move the file Otherwise you may get an error !')

lb1 = tk.Label(w1,text = 'Img2pdf Converter',font = ('Fira Code',10,'bold'),fg = "#F9D342",bg = "#292826")
lb1.pack(padx = 2,pady = 10)

def select():
    global files1                                                        
    files1 = fd.askopenfilenames()

def select_location():
    global file_location
    file_location = fd.askdirectory()

def move_file():
    if e1.get() == '' or file_location == '':
        mg.showwarning('Application Error','Either the file is not renamed or Location is not selected !')
    else:
        new_location = file_location + "/" + e1.get() + ".pdf"
        current_dir = os.getcwd()  + "/" + e1.get() + ".pdf"
        shutil.move(current_dir,new_location)

btn1 = tk.Button(w1,text = 'Select Image/Images',command = select,bg = "#F9D342",fg = "#292826")
btn1.pack(padx = 2,pady = 5)

frm1 = tk.Frame(w1,bg = "#292826")
frm1.pack(padx = 2,pady = 3)

lb2 = tk.Label(frm1,text = 'Rename File',fg = "#F9D342",bg = '#292826',font = ('Fira Code',10,'bold'))
lb2.pack(padx = 2,pady = 3)

e1 = tk.Entry(frm1)
e1.pack(padx = 2,pady = 10)

def convert_single():
    for index, file_name in enumerate(files1):                                      
        
        if '.' in e1.get():
            mg.showwarning('Application Warning','Do not use . while giving file name !')                                       

        elif e1.get() == "" or file_location == '':
            mg.showwarning('Application Warning','Please fill out the name of pdf file or select file location !')                           
        
        else:
            with open("{filename}.pdf".format(filename = e1.get()),"wb") as f:      
                f.write(img.convert(file_name))

def convert_multiple():
    if e1.get() == '' or file_location == '':
        mg.showwarning('Application Warning','Please fill out the name of pdf file or select file location !')   

    elif '.' in e1.get():
        mg.showwarning('Application Warning','Do not use . while giving file name !')              

    else:
        with open("{file}.pdf".format(file = e1.get()),"wb") as f:     
            f.write(img.convert(files1))

btn4 = tk.Button(frm1,text = 'Select Location',bg = "#F9D342",fg = "#292826",command = select_location)
btn4.pack(padx = 3,pady = 3)                          

btn2 = tk.Button(frm1,text = 'Convert Image',command = convert_single,bg = "#F9D342",fg = "#292826")       
btn2.pack(side = 'left',padx = 5,pady = 3)

btn3 = tk.Button(frm1,text = 'Convert Images',command = convert_multiple,bg = "#F9D342",fg = "#292826") 
btn3.pack(side = 'right',padx = 3,pady = 3)

btn5 = tk.Button(w1,text = 'Move File',command = move_file,bg = "#F9D342",fg = "#292826")
btn5.pack(padx = 3,pady = 3)

w1.mainloop()