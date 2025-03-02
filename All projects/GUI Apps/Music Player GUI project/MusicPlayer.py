import tkinter as tk
from tkinter import messagebox
import os,pygame

# Windows setup
app = tk.Tk()
app.geometry("300x333")
app.title("Music player")
app.configure(bg="black")

# Main Variables
sound_folder_path = ""
try:
    files = [f for f in os.listdir(sound_folder_path) if os.path.isfile(os.path.join(sound_folder_path, f)) and f.endswith(".mp3")]
except Exception as e:
    print(f"Error: {e}")
current_index = 0
current_file = ""
try:
    pygame.mixer.init()
    sound = pygame.mixer.Sound(sound_folder_path + "/" + current_file)
except:
    print("No .mp3 found")

clicked_pause = True

playing_sound = False

# All Functions
def display_current_song_name():
    pass

def pause():
    pass

def next():
    pass

def back():
    pass

def acess_folder():
    pass

def play_sound():
    pass

def check_if_finished():
    pass

# Frames
frame1 = tk.Frame(app,bg="#151515")
frame2 = tk.Frame(app,bg="black")

# GUI Elements
current_song_name_text = tk.Label(app,text="No song selected",font=("Roman",15),bg="#013000",fg="white")
pause_button = tk.Button(frame1,text="▶",bg="white",font=("",11),anchor="center", width=4,height=2,command=pause)
next_button = tk.Button(frame1,text=">",anchor="center",command=next)
back_button = tk.Button(frame1,text="<",anchor="center",command=back)
path_folder_input = tk.Entry(frame2,width=25)
path_folder_input.insert(0,"C:Enter/a/folder/path/here")
set_folder_button = tk.Button(frame2,text="ACCES FOLDER")

# Updated functions
def play_sound():
    global clicked_pause,sound,start_time,playing_sound,current_file,sound_folder_path
    if not clicked_pause:
        if not playing_sound:
            sound.play()
            playing_sound = True
    else:
        if playing_sound:
            sound.stop()
            playing_sound = False

def pause():
    global clicked_pause,sound,pause_time,playing_sound
    if clicked_pause:
        pause_button.config(text="II")
        clicked_pause = False
        if not playing_sound:
            sound.play()
            playing_sound = True
    else:
        pause_button.config(text="▶")
        clicked_pause = True
        if playing_sound:
            sound.stop()
            playing_sound = False
    play_sound()

def next():
    global current_index,current_file,files,current_song_name_text,sound,playing_sound
    if current_index > len(files) - 1:
        current_index = 0
    else:
        current_index += 1 
    current_file = files[current_index]
    current_song_name_text.config(text=current_file)
    sound.stop()
    playing_sound = False
    sound = pygame.mixer.Sound(sound_folder_path + "/" + current_file)
    pause()


def back():
    global current_index,files,current_file,sound,playing_sound
    if current_index < 0:
        current_index = len(files) - 1
    else:
        current_index -= 1
    current_file = files[current_index]
    current_song_name_text.config(text=current_file)
    sound.stop()
    playing_sound = False
    sound = pygame.mixer.Sound(sound_folder_path + "/" + current_file)
    pause()


def acess_folder():
    global current_index,current_file,files,sound_folder_path,path_folder_input,sound
    sound_folder_path = path_folder_input.get()
    
    try:
        files = [f for f in os.listdir(sound_folder_path) if os.path.isfile(os.path.join(sound_folder_path, f)) and f.endswith(".mp3")]
        print(f"Files accesed succesfully: {files}")
        pygame.mixer.init()
    except Exception as e:
        messagebox.showerror("Error",f"A error has occuried when you wanted to acces a folder: {e}")

    current_file = files[0]
    sound = pygame.mixer.Sound(sound_folder_path + "/" + current_file)
    current_song_name_text.config(text=current_file)

def check_if_finished():
    global playing_sound
    if not pygame.mixer.get_busy() and playing_sound:
        playing_sound = False
        next()
    app.after(1000,  check_if_finished)
        

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