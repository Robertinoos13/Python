"""
    Hello and thanks because you take a look at this code!
    This is a simple alarm GUI with TKINTER(Main Library) and PYGAME(for the sound).This looks more like a temporizer than a alarm,
but you can use it as a alarm too,because for what you need to set the alarm at a specific time on a laptop lol?
    At this code,you have features,like: Inversed time count,alarm message,repeat mode,set a sound for your alarm and a help window.
    I hope the code is not really hard to understand,so you can modify and make 'little experiments' on it as you want.
    Follom me on GitHub and TikTok(@robert_de_romania) to support me if you want :)

"""


import tkinter as tk
from tkinter import messagebox
import pygame

# Setup window
app = tk.Tk()
app.title('Alarm GUI')
app.geometry('300x200')

help_app = tk.Frame()

# Main variables
time = 0
time_saved = time
message = "You entered no message,so your alarm was stopped right now"
repeat = False
started = False
audio_file_path = "C:/Enter/here/your/sound/file/path.mp3"
try:
    pygame.mixer.init()
    sound = pygame.mixer.Sound(audio_file_path)
except FileNotFoundError:
    messagebox.showerror("File Error","You don't have a sound for your alarm,its not really a big problem,but if you want to listen when the alarm is ready,its recomanded to set a .mp3 file path")

# All funtions
def time_lore(): # Update the "time_text" Label(text) with the current time
    pass

def set_time(): # Steals the value from "time_input" and sets it to time
    pass

def set_message(): # Steals the value from "message_input" and sets it to alarm message
    pass

def set_music(): # Steals the value from "music_input" and sets it to audio_file_path
    pass

def start_and_stop(): # Start and stop the alarm when the function is called
    pass

def put_repeated(): # Put the value of the "repeat" variable to True or False
    pass

def open_help_window(): # Open the help window
    pass

# Frames
frame1 = tk.Frame(app)
frame2 = tk.Frame(app)
frame3 = tk.Frame(app)
frame4 = tk.Frame(app)

# Elements
time_text = tk.Label(app, text=f'{time // 60}:{time % 60}' if time % 60 > 9 else f"{time // 60}:0{time % 60}", font=('Impact', 22))

time_input = tk.Entry(frame1, font=("Arial",11),width=26,justify="center")
time_input.insert(0, "Enter here your time in seconds")
# time_input.bind("<FocusIn>", lambda args: time_input.delete('0', 'end')) # Uncomment this line to delete the text when the user clicks on the Entry

okay_button1 = tk.Button(frame1, text="Set")

message_input = tk.Entry(frame2, font=("Arial",11), width=26, justify="center")
message_input.insert(0, "Enter a message for your alarm")
# message_input.bind("<FocusIn>", lambda args: time_input.delete('1', 'end')) # Uncomment this line to delete the text when the user clicks on the Entry

okay_button2 = tk.Button(frame2,text="Set")

music_input = tk.Entry(frame4, font=("Arial",11), width=26, justify="center")
music_input.insert(0, "Enter the path of your music file (mp3)")
okay_button3 = tk.Button(frame4,text="Set")

start_stop_button = tk.Button(frame3,text="START",command=start_and_stop,bg="green",fg="white")
repeated_text = tk.Label(frame3,text="REPEAT:")
repeated_button = tk.Button(frame3,text="❎",bg="red",fg="white")
help_text = tk.Label(frame3,text="GET HELP")
help_button = tk.Button(frame3,text="❔",bg="#6de7dd")


# Updated Functions
def time_lore(): # Update the "time_text" Label(text) with the current time
    global time,time_saved,started,repeat,message,sound
    if time <= 0 and not started:
        time = 1
        started = False
        start_stop_button.config(text="START",bg="green")
        time_text.config(text=f"{time // 60}:{time % 60}" if time % 60 > 9 else f"{time // 60}:0{time % 60}")
        time_lore()
    elif time > 0 and started:
        time -= 1
        time_text.config(text=f"{time // 60}:{time % 60}" if time % 60 > 9 else f"{time // 60}:0{time % 60}")
        time_text.after(1000,time_lore)
    elif time <= 0 and started:
        time = 1
        started = False
        start_stop_button.config(text="STOP",bg="red")
        try:
            sound = pygame.mixer.Sound(audio_file_path)
            sound.play()
            messagebox.showinfo("Alarm",message)
            sound.stop()
        except NameError:
            messagebox.showinfo("Alarm",message)
        if repeat:
            started = True
            start_stop_button.config(text="STOP",bg="red")
            time = time_saved
            time_lore()
        else:
            started = False
            time_text.config(text=f"{time // 60}:{time % 60}" if time % 60 > 9 else f"{time // 60}:0{time % 60}")
            start_stop_button.config(text="START",bg="green")

def start_and_stop(): # Start and stop the alarm when the function is called
    global started,start_stop_button,time_saved,time
    time_saved = time
    if not started:
        started = True
        start_stop_button.config(text="STOP",bg="red")
    elif started:
        started = False
        start_stop_button.config(text="START",bg="green")
    time_lore()

def put_repeated(): # Put the value of the "repeat" variable to True or False
    global repeat,repeated_button
    if not repeat:
        repeat = True
        repeated_button.config(text="✅",bg="green")
    elif repeat:
        repeat = False
        repeated_button.config(text="❎",bg="red")

def set_time(): # Steals the value from "time_input" and sets it to time
    global time,time_saved,time_text
    try:
        time = int(time_input.get())
        time_text.config(text=f"{time // 60}:{time % 60}" if time % 60 > 9 else f"{time // 60}:0{time % 60}")
        time_saved = time
    except:
        messagebox.showerror("Error","You entered a invalid time value, please enter a float or integer value")

def set_message(): # Steals the value from "message_input" and sets it to alarm message
    global message
    message = message_input.get()

def open_help_window():
    help_window = tk.Toplevel(app)
    help_window.title("Help")
    help_window.geometry("1400x555")
    help_title = tk.Label(help_window, text="This is the help window.", font=("Impact", 22))
    help_title.pack(pady=(0,33),anchor="n")
    help_subtitle1 = tk.Label(help_window, text="What is with 'Set' buttons?", font=("Arial Black", 15))
    help_subtitle1.pack(anchor="nw",pady=1)
    help_text1 = tk.Label(help_window, text="     The 'Set' buttons are used to set the time, message and music file path for the alarm,by stealing values from input fields.", font=("Arial", 11))
    help_text1.pack(anchor="w",pady=(1,11))
    help_subtitle2 = tk.Label(help_window, text="What is with 'Repeat' mode?", font=("Arial Black", 15))
    help_subtitle2.pack(anchor="nw",pady=1)
    help_text2 = tk.Label(help_window, text="     The 'repeat' mode, when switched on, the alarm will repeat the time you set last time every time it reaches 0, so you won't have to press the start button again until this repeat mode is off off", font=("Arial", 11))
    help_text2.pack(anchor="w",pady=(1,11))
    help_subtitle3 = tk.Label(help_window, text="What is with first Input Field for?", font=("Arial Black", 15))
    help_subtitle3.pack(anchor="nw",pady=1)
    help_text3 = tk.Label(help_window, text="     The first Input Field is for enter a integer value for your alarm time (on seconds).", font=("Arial", 11))
    help_text3.pack(anchor="w",pady=(1,11))
    help_subtitle4 = tk.Label(help_window, text="What is with second Input Field for?", font=("Arial Black", 15))
    help_subtitle4.pack(anchor="nw",pady=1)
    help_text4 = tk.Label(help_window, text="     The second Input Field is for enter a 'ready alarm' message (string).This value will be showed when the alarm is ready.", font=("Arial", 11))
    help_text4.pack(anchor="w",pady=(1,11))
    help_subtitle5 = tk.Label(help_window, text="What is with third Input Field for?", font=("Arial Black", 15))
    help_subtitle5.pack(anchor="nw",pady=1)
    help_text5 = tk.Label(help_window, text="     The third Input Field is for enter a sound path from your computer.The sound will be played when the alarm is ready.For example,a path looks like this: C:/Users/John/Desktop/All Folders/Programs/Python", font=("Arial", 11))
    help_text5.pack(anchor="w",pady=(1,11))
    help_subtitle6 = tk.Label(help_window, text="What i need to do if i can't click on a Input Field?", font=("Arial Black", 15))
    help_subtitle6.pack(anchor="nw",pady=1)
    help_text6 = tk.Label(help_window, text="     To fix this problem,you can click on any buttons from the alarm (like Sets buttons,start/stop button,ect) or close the help window and try again", font=("Arial", 11))
    help_text6.pack(anchor="w",pady=(1,11))

help_button.config(command=open_help_window)

def set_music(): # Steals the value from "music_input" and sets it to audio_file_path
    global audio_file_path,music_input
    try:
        audio_file_path = music_input.get()
        pygame.mixer.init()
        sound = pygame.mixer.Sound(audio_file_path)
        messagebox.showinfo("Succes","The sound file was set succesfully")
    except:
        messagebox.showerror("Error","The sound file path is invalid,please enter a valid path")
    
okay_button3.config(command=set_music)

# Packs
time_text.pack(pady=(0,10))

frame1.pack()
time_input.pack(side=tk.LEFT)
okay_button1.config(command=set_time)
okay_button1.pack(side=tk.RIGHT)

frame2.pack()
message_input.pack(side=tk.LEFT)
okay_button2.config(command=set_message)
okay_button2.pack(side=tk.RIGHT)

frame3.pack(side=tk.TOP,pady=5,anchor="w")
help_text.pack(side=tk.RIGHT)
help_button.pack(side=tk.RIGHT,padx=(22,0))
start_stop_button.config(command=start_and_stop)
start_stop_button.pack(side=tk.RIGHT)
repeated_button.config(command=put_repeated)
repeated_button.pack(side=tk.RIGHT,padx=(0,22),anchor="w")
repeated_text.pack(side=tk.LEFT,padx=(26,0))

frame4.pack(anchor="s")
music_input.pack(side=tk.LEFT)
okay_button3.pack(side=tk.RIGHT)


tk.mainloop()