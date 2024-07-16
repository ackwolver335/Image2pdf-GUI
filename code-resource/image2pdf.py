import tkinter as tk
import tkinter.filedialog as fd
import img2pdf as img

w1 = tk.Tk()

w1.title('Image To PDF Converter')
w1.geometry('300x190')                
w1.resizable(False,False)                               
w1.config(background = "#292826")              

lb1 = tk.Label(w1,text = 'Img2pdf Converter',font = ('Fira Code',10,'bold'),fg = "#F9D342",bg = "#292826")
lb1.pack(padx = 2,pady = 10)

def select():
    global files1                                                              
    files1 = fd.askopenfilenames(initialdir = '/',title = 'Select files')

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
            with open(f"file {index}.pdf","wb") as f:                      
                f.write(img.convert(file_name))                                         

        elif e1.get() == "":
            with open("single.pdf","wb") as f:          
                f.write(img.convert(file_name))                            
        
        else:
            with open("{filename}.pdf".format(filename = e1.get()),"wb") as f:      
                f.write(img.convert(file_name))                           

def convert_multiple():
    if e1.get() == '':
        with open("file.pdf","wb") as f:    
            f.write(img.convert(files1))   

    elif '.' in e1.get():
        with open("file.pdf","wb") as f:   
            f.write(img.convert(files1))             

    else:
        with open("{file}.pdf".format(file = e1.get()),"wb") as f:     
            f.write(img.convert(files1))                          

btn2 = tk.Button(frm1,text = 'Convert Image',command = convert_single,bg = "#F9D342",fg = "#292826")       
btn2.pack(side = 'left',padx = 5)

btn3 = tk.Button(frm1,text = 'Convert Images',command = convert_multiple,bg = "#F9D342",fg = "#292826") 
btn3.pack(side = 'right',padx = 3)

w1.mainloop()