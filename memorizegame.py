"""
    Hello and thanks because you take a look on this code.
    This is a simple game that I made in Python using Tkinter and Random libraries.More exactly, this is a memory game
where you have to memorize the colors that will be displayed on the screen and then you have to press the colors
in a correct order. If you press the colors in a wrong order, you will lose the game and you will have to start again.
You can also see the best score and the current score on the screen. The best score will be updated only if the current
score is higher than the best score.
    Follow me on GitHub and TikTok(@robert_de_romania) if you want to support me :)
"""

import tkinter as tk
import random

# Windows setup
root = tk.Tk()
root.title("Memorize game")
root.geometry("500x500")

# Main variables
best_score = 0
current_score = 0
global_index = current_score

game_started = False
can_select = False
can_continue = True
selected = False
show_ready = False

probability_choice = ("b","r","g","o","p") # b-blue ; r-red ; g-green ; o-orange ; p-purple
selected_choices = [] # Here will be selected random colors to memorize
user_choices = [] # Here will be saved the entered values by USER

# All Functions
def game_lore():
    pass

def modify_start_button():
    pass

def start_game():
    global game_started,lose,can_continue,can_select,selected,show_ready,best_score,global_index
    if not game_started:
        game_started = True
        lose = False
        selected_choices.clear()
        user_choices.clear()
        best_score = 0
        current_score = 0
        global_index = current_score
        can_select = False
        can_continue = True
        selected = False
        show_ready = False
    elif game_started:
        selected_choices.clear()
        user_choices.clear()
        game_started = False

    modify_start_button()

def blue_input_system():
    pass

def red_input_system():
    pass

def green_input_system():
    pass

def orange_input_system():
    pass

def purple_input_system():
    pass

# Frames
frame1 = tk.Frame(root)
frame2 = tk.Frame(root)

# Elements
start_button = tk.Button(root,text="START GAME",width=11,height=2,command=start_game)
statusgame_text = tk.Label(root,text=f"The game has not started yet",font=("Arial",20),height=5)
best_score_text = tk.Label(root,text=f"BEST SCORE: {best_score}")
current_score_text = tk.Label(root,text=f"CURRENT SCORE: {current_score}")

# Updated Functions
def game_lore():
    global game_started, selected_choices, user_choices, probability_choice, current_score, best_score, statusgame_text
    selected_color = ""
    if game_started:
        root.after(1000, lambda: statusgame_text.config(text="Get Ready."))
        root.after(2000, lambda: statusgame_text.config(text="Get Ready.."))
        root.after(3000, lambda: statusgame_text.config(text="Get Ready..."))
        root.after(4000, lambda: statusgame_text.config(text="Let's go!"))
        root.after(5000, lambda: statusgame_text.config(text="Memorize this..."))

        selected_color = random.choice(probability_choice).lower()
        selected_choices.append(selected_color)

        def view_color(index=0):
            if index < len(selected_choices):
                color = selected_choices[index]
                if color == "b":
                    blue_button.config(bg="lightblue")
                    root.after(1111, lambda: blue_button.config(bg="blue"))
                elif color == "r":
                    red_button.config(bg="#FF9999")
                    root.after(1111, lambda: red_button.config(bg="red"))
                elif color == "g":
                    green_button.config(bg="lightgreen")
                    root.after(1111, lambda: green_button.config(bg="green"))
                elif color == "o":
                    orange_button.config(bg="yellow")
                    root.after(1111, lambda: orange_button.config(bg="orange"))
                elif color == "p":
                    purple_button.config(bg="plum")
                    root.after(1111, lambda: purple_button.config(bg="purple"))
                root.after(1500, lambda: view_color(index + 1))
            else:
                global can_select
                can_select = True
                statusgame_text.config(text="Okay, your turn!")

        root.after(6000, view_color)

def verify_if_correct():
    pass

def blue_input_system():
    global user_choices,can_select,selected
    print("Blue button pressed")
    if game_started and can_select:
        user_choices.append("b")
        selected = True
        verify_if_correct()
    elif not game_started:
        statusgame_text.config(text="The game has not started yet")
    elif game_started and not can_select:
        statusgame_text.config(text="Wait for buttons...")

def red_input_system():
    global user_choices,can_select,selected
    print("Red button pressed")
    if game_started and can_select:
        user_choices.append("r")
        selected = True
        verify_if_correct()
    elif not game_started:
        statusgame_text.config(text="The game has not started yet")
    elif game_started and not can_select:
        statusgame_text.config(text="Wait for buttons...")

def green_input_system():
    global user_choices,can_select,selected
    print("Green button pressed")
    if game_started and can_select:
        user_choices.append("g")
        selected = True
        verify_if_correct()
    elif not game_started:
        statusgame_text.config(text="The game has not started yet")
    elif game_started and not can_select:
        statusgame_text.config(text="Wait for buttons...")

def orange_input_system():
    global user_choices,can_select,selected
    print("Orange button pressed")
    if game_started and can_select:
        user_choices.append("o")
        selected = True
        verify_if_correct()
    elif not game_started:
        statusgame_text.config(text="The game has not started yet")
    elif game_started and not can_select:
        statusgame_text.config(text="Wait for buttons...")

def purple_input_system():
    global user_choices,can_select,selected
    print("Purple button pressed")
    if game_started and can_select:
        user_choices.append("p")
        selected = True
        verify_if_correct()
    elif not game_started:
        statusgame_text.config(text="The game has not started yet")
    elif game_started and not can_select:
        statusgame_text.config(text="Wait for buttons...")

def modify_start_button():
    global start_button,game_started
    if game_started:
        start_button.config(text="STOP GAME")
    elif not game_started:
        start_button.config(text="START GAME")
    game_lore()

def verify_if_correct():
    global lose,selected,can_select,current_score,best_score,global_index,can_continue
    print("A color button was pressed")
    selected = False
    if user_choices[global_index] == selected_choices[global_index]:
        global_index += 1
        message = random.choice(["Nice!","Good!","Perfect!","Not Bad!","Great!","Cool!","Awesome!"])
        statusgame_text.config(text=f"{message}")
    elif user_choices[global_index] != selected_choices[global_index]:
        global_index = 0
        can_continue = False
        print(f"{user_choices} is not equals with {selected_choices}")
        selected_choices.clear()
        user_choices.clear()
        statusgame_text.config(text="Oh,you lose.GAME OVER")
        lose = True
        if current_score > best_score:
            best_score = current_score
            current_score = 0
            current_score_text.config(text=f"CURRENT SCORE: {current_score}")
            best_score_text.config(text=f"BEST SCORE: {best_score}")
        if lose:
            global game_started
            game_started = False
            if not game_started:
                start_button.config(text="TRY AGAIN")

    if len(user_choices) == len(selected_choices) and can_continue:
        can_select = False
        global_index = 0
        if user_choices == selected_choices:
            statusgame_text.config(text="Good,lets cook the next level")
            current_score += 1
            current_score_text.config(text=f"CURRENT SCORE: {current_score}")
            user_choices.clear()
            game_lore()
        else:
            selected_choices.clear()
            user_choices.clear()
            statusgame_text.config(text="Oh,you lose.GAME OVER")
            lose = True
            if current_score > best_score:
                best_score = current_score
                current_score = 0
                current_score_text.config(text=f"CURRENT SCORE: {current_score}")
                best_score_text.config(text=f"BEST SCORE: {best_score}")
            if lose:
                global_index = 0
                game_started = False
                if not game_started:
                    start_button.config(text="TRY AGAIN")

# Main Buttons
blue_button = tk.Button(frame1,width=11,height=5,bg="blue",command=blue_input_system)
red_button = tk.Button(frame1,width=11,height=5,bg="red",command=red_input_system)
green_button = tk.Button(frame1,width=11,height=5,bg="green",command=green_input_system)
orange_button = tk.Button(frame1,width=11,height=5,bg="orange",command=orange_input_system)
purple_button = tk.Button(frame1,width=11,height=5,bg="purple",command=purple_input_system)

# Packs (add the elements on GUI)
statusgame_text.pack()
frame1.pack()
blue_button.pack(side=tk.LEFT,padx=1)
red_button.pack(side=tk.LEFT,padx=1)
green_button.pack(side=tk.LEFT,padx=1)
orange_button.pack(side=tk.LEFT,padx=1)
purple_button.pack(side=tk.LEFT,padx=1)
start_button.pack(pady=11)
best_score_text.pack()
current_score_text.pack()

root.mainloop()