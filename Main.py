from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import tkinter as tk
from Images_Processor import *
from QR_Reader import main


inputd =''
outputd =''

def open_output_folder(): 
    global outputd
    folder_path = filedialog.askdirectory()
    outputd = folder_path
    print("Selected Directory:", folder_path)

def open_input_folder():
    folder_path = filedialog.askdirectory()
    global inputd
    inputd= folder_path


def runit():
    main(inputd, outputd)
    tk.messagebox.showinfo('Success','Successful!')
    root.destroy()

root = Tk()
frm = ttk.Frame(root, padding=50)
frm.grid()
ttk.Button(frm, text = 'Select input folder', command = open_input_folder).grid(column= 1, row=0)
ttk.Button(frm, text = 'Select output folder', command = open_output_folder).grid(column= 1, row=1)
ttk.Button(frm, text = 'Generate .csv', command = runit).grid(column= 1, row=3)
root.mainloop()
