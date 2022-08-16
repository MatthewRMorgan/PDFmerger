import tkinter as tk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from PyPDF2 import PdfMerger
import os

#global var for filenames
files = []

def UploadAction(event=None):
    filename = fd.askopenfilename()
    print('Selected:', filename)

def combine_files():
    combinedFileName = "combinedPDF.pdf"
    if (files == []):
        showinfo("ERROR: no files selected")
        return 0
    merger = PdfMerger()
    for file in files:
        merger.append(file)
    merger.write(combinedFileName)
    merger.close()
    filetypes = (
        ('PDF', '*.pdf'),
    )

    savedFile = fd.asksaveasfile(filetypes = filetypes, defaultextension = filetypes)
    savedFileAddress = savedFile.name
    savedFile.close()
    os.remove(savedFile.name)
    #save file address, delete file, then move file from here to spot using rename
    os.rename(combinedFileName, savedFileAddress)
    #os.remove(combinedFileName)

def open_files():
    global files
    files = []
    filetypes = (
        ('PDF', '*.pdf'),
    )

    filenames = fd.askopenfilenames(
        title='Open a file',
        filetypes=filetypes)
    for i in range(len(filenames)):
        label = tk.Label(
            text=filenames[i],
            fg="black",
            bg="green",
            width=20,
            height=3
        )
        label.pack(fill=tk.X)
        #label.config(text=filename)
    files = filenames


window = tk.Tk()
window.title("PDF merger")
#window.geometry('700x700')

frame1 = tk.Frame(master=window, height=30, bg="black")
frame1.pack(fill=tk.X)

button = tk.Button(
    text="select PDFs",
    width=15,
    height=3,
    bg="grey",
    fg="white",
    command=open_files
)


button2 = tk.Button(
    text="combine PDFs",
    width=15,
    height=3,
    bg="grey",
    fg="white",
    command=combine_files
)
label = tk.Label(
    text="",
    fg="black",
    bg="green",
    width=30,
    height=10
)

button.pack(expand=True)
frame2 = tk.Frame(master=window, height=50, bg="grey")
#label.pack()
frame2.pack(fill=tk.X)
button2.pack()

window.mainloop()

print("goodbye")
print(files)