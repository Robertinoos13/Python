import tkinter as tk
from tkinter import messagebox
import os,pygame

# Windows setup
app = tk.Tk()
app.geometry("300x333")
app.title("Music Player")
app.configure(bg="black")

# Main Variables
sound_folder_path = ""
try:
    files = [f for f in os.listdir(sound_folder_path) if os.path.isfile(os.path.join(sound_folder_path, f)) and f.endswith(".mp3")]
except Exception as e:
    print(f"Error: {e}")
current_index = 0
current_file = ""

pygame.mixer.init()
    

clicked_pause = True

playing_sound = False

# Frames
frame1 = tk.Frame(app,bg="#151515")
frame2 = tk.Frame(app,bg="black")

# GUI Elements
current_song_name_text = tk.Label(app,text="No song selected", font=("Roman",15), bg="#013000", fg="white", wraplength=300)
pause_button = tk.Button(frame1,text="▶", bg="white", font=("",11), anchor="center", width=4,height=2)
next_button = tk.Button(frame1,text=">", anchor="center", command=next)
back_button = tk.Button(frame1,text="<", anchor="center")
path_folder_input = tk.Entry(frame2, width=25)
path_folder_input.insert(0,"C:Enter/a/folder/path/here")
set_folder_button = tk.Button(frame2, text="ACCES FOLDER")

# All functions

def play_sound():
    global clicked_pause,playing_sound,current_index
    
    if not files:
        messagebox.showerror("Error","No .mp3 files in the folder :(")
        return
    
    pygame.mixer.music.load(os.path.join(sound_folder_path, files[current_index]))
    pygame.mixer.music.play()
    playing_sound = True
    clicked_pause = False
    pause_button.config(text="II")

def pause():
    global clicked_pause,playing_sound

    if clicked_pause:
        pygame.mixer.music.unpause()
        pause_button.config(text="II")
        clicked_pause = False
        playing_sound = True
    else:
        pygame.mixer.music.pause()
        pause_button.config(text="▶")
        clicked_pause = True
        playing_sound = False


def next():
    global current_index, playing_sound, clicked_pause

    if not files:
        return
    
    current_index = (current_index + 1) % len(files)
    clicked_pause = False
    playing_sound = True
    update_song()


def back():
    global current_index, clicked_pause, playing_sound
    if not files:
        return
    
    current_index = (current_index - 1) % len(files)

    clicked_pause = False
    playing_sound = True
    update_song()

back_button.config(command=back)

def update_song():
    global playing_sound

    if files:
        current_song_name_text.config(text=files[current_index])
        pygame.mixer.music.stop()
        playing_sound = False
        play_sound()

def acess_folder():
    global current_index,files,sound_folder_path,path_folder_input,sound

    sound_folder_path = path_folder_input.get()

    if not os.path.isdir(sound_folder_path):
        messagebox.showerror("Error", "Invalid folder path")
        return
    
    files = [f for f in os.listdir(sound_folder_path) if f.endswith(".mp3")]

    if not files:
        messagebox.showerror("Error", "No .mp3 files found here")

    current_index = 0
    update_song()

def check_if_finished():
    global playing_sound
    if not pygame.mixer.music.get_busy() and playing_sound:
        next()
    app.after(1000, check_if_finished)
    print(current_index)    

# Pack elements
current_song_name_text.pack(pady=11)
frame1.pack(pady=22)
next_button.config(command=next)
next_button.pack(side=tk.RIGHT,padx=5)
pause_button.config(command=pause)
pause_button.pack(side=tk.RIGHT,padx=5)
back_button.config(command=back)
back_button.pack(side=tk.RIGHT,padx=5)
frame2.pack()
path_folder_input.pack(side=tk.LEFT,padx=1)
set_folder_button.config(command=acess_folder)
set_folder_button.pack(side=tk.LEFT,padx=1)

app.after(1000, check_if_finished)
app.mainloop()