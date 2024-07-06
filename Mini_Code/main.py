from pytube import *
from tkinter.filedialog import *
from tkinter import *
from tkinter.messagebox import *
from threading import *
import time

file_size = 0

def progress(stream=None, chunk=None, file_handle=None, remaining=None):
    file_downloaded = (file_size - file_handle)
    per = (file_downloaded / file_size) * 100
    dBtn.config(text="{:00.0f} % downloaded".format(per))

def startDownload():
    global file_size
    try:
        url = urlField.get()
        print(url)
        dBtn.config(text='Please wait...')
        dBtn.config(state=DISABLED)
        path_to_save = askdirectory()
        print(path_to_save)
        if path_to_save is None:
            return

        # Create a YouTube object
        ob = YouTube(url, on_progress_callback=progress)

        # Choose the highest quality stream available
        strm = ob.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        
        file_size = strm.filesize
        vTitle.config(text=strm.title)
        vTitle.pack(side=TOP)

        # Delayed start
        schedule_time = int(entry_time.get())  # Get the scheduled time from the Entry widget
        time.sleep(schedule_time)  # Sleep until the scheduled time

        strm.download(path_to_save)
        print("done")
        dBtn.config(text='Start Download')
        dBtn.config(state=NORMAL)
        showinfo("Download Finished!")
        urlField.delete(0, END)
        vTitle.pack_forget()

    except Exception as e:
        print(e)
        print("error")

def startDownloadThread():
    thread = Thread(target=startDownload)
    thread.start()

main = Tk()

main.title("YouTube Downloader")
main.iconbitmap('utube.ico')
main.geometry("500x600")

file = PhotoImage(file='youtube.png')
headingIcon = Label(main, image=file)
headingIcon.pack(side=TOP)

urlField = Entry(main, font=("verdana", 18), justify=CENTER)
urlField.pack(side=TOP, fill=X, padx=10, pady=20)

entry_time = Entry(main, font=("verdana", 18), justify=CENTER)
entry_time.pack(side=TOP, fill=X, padx=10, pady=20)
entry_time.insert(0, "Enter delay in seconds")  # Default text

dBtn = Button(main, text="Start Download", font=("verdana", 18), relief='ridge', command=startDownloadThread)
dBtn.pack(side=TOP)

vTitle = Label(main, text="Video title")
main.mainloop()
