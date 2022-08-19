from pytube import YouTube
from tkinter import *
from tkinter import ttk
import os

def youtubedl(*args):
    checkGet = check.get()
    yt = YouTube(link.get())


    if checkGet == 'True':
        stream = yt.streams.filter(only_audio=True).first()
        out_file = stream.download('./')
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
    else:
        stream = yt.streams.get_highest_resolution()
        stream.download('./')


root = Tk()
root.title('Youtube Downloader')

mainframe = ttk.Frame(root, padding = "3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainframe, text="Insert Link").grid(column=1, row=1, sticky=E)
link = StringVar()
link_entry = ttk.Entry(mainframe, width=7, textvariable=link)
link_entry.grid(column=2, row=1, sticky=(W, E))

check = StringVar()
checkbox = ttk.Checkbutton(mainframe, text='Audio Only', variable=check, onvalue='True', offvalue='False')
checkbox.grid(column=2, row=2, sticky=(W,E))

ttk.Button(mainframe, text="Download", command=youtubedl).grid(column=3, row=2, sticky=(E, W))

for child in mainframe.winfo_children():
    child.grid_configure(padx=10, pady=10)

link_entry.focus()
root.bind("<Return>", youtubedl)

root.mainloop()
