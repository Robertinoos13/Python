"""
    Hello and thank because you take a look at this script
    This script, its a game with a GUI. More exactly, its a colors game where you need to guess the order of colors. As indice to guess more easy the order of colors,
at all verifies, the script says you how much colors you guessed their correct order, modify and verify while you guess all colors on a correct order. Try to get
less tries than other rounds/games to make a personal record.
    Follow me on GitHub and TikTok (@robert_de_romania) if you want to support me on my scripts works :) 
"""

import tkinter as tk
import random

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Main Variables
        default_width_colors = 5
        default_height_colors = 2

        self.all_colors = ["black", "red", "yellow", "blue", "green", "pink", "orange", "purple", "cyan", "darkblue", "lightgreen", "lightblue", "blueblack", "darkgreen", "lightbrown", "darkred", "clearblue", "goldmetal"]
        self.colors_choosed_by_calculator = [] # RANDOM library will modify this
        self.colors_choosed_by_user = ["?", "?", "?", "?", "?"] # User will modify this
        self.on_modify_index = -1

        self.game_started = False

        self.can_the_player_choose_a_num = False
        self.has_selected_a_num = False
        self.can_the_player_choose_a_color = False
        self.can_verify = False

        self.winner = False

        self.tries_this_round = 0
        self.rounds_played = 0
        self.num_of_wins = 0

        # Window setup
        self.title("Guess Colors Game")
        self.geometry("555x311")
        self.config(bg="#e6dddd")

        # Frames
        frame1 = tk.Frame(self, bg="white")
        frame2 = tk.Frame(self, bg="white")
        frame3 = tk.Frame(self, bg="#e6dddd")
        frame4 = tk.Frame(self, bg="white")
        frame5 = tk.Frame(self, bg="white")
        frame6 = tk.Frame(self, bg="white")
        frame7 = tk.Frame(self, bg="white")
        
        # Elements
        self.status_text = tk.Label(frame1, text="The game has not started yet", font=("Arial",15), wraplength=300)

        black_button = tk.Button(frame1,bg="black",width= default_width_colors,height= default_height_colors, command=self.black_button_function)
        red_button = tk.Button(frame1, bg="red", width= default_width_colors,height= default_height_colors, command=self.red_button_function)
        yellow_button = tk.Button(frame1, bg="yellow", width= default_width_colors, height= default_height_colors, command=self.yellow_button_function)

        blue_button = tk.Button(frame2, bg="blue", width= default_width_colors, height= default_height_colors, command=self.blue_button_function) 
        green_button = tk.Button(frame2, bg="green", width= default_width_colors, height= default_height_colors, command=self.green_button_function)
        pink_button = tk.Button(frame2, bg="pink", width= default_width_colors, height= default_height_colors, command=self.pink_button_function)

        orange_button = tk.Button(frame3, bg="orange", width= default_width_colors, height= default_height_colors, command=self.orange_button_function)
        purple_button = tk.Button(frame3, bg="purple", width= default_width_colors, height= default_height_colors, command=self.purple_button_function)
        cyan_button = tk.Button(frame3, bg="cyan", width= default_width_colors, height= default_height_colors, command=self.cyan_button_function)
        self.neutral_button1 = tk.Button(frame3, bg="darkgray", width=5, height=1, text="1", font="Impact", command=self.neutral_button_1)
        self.neutral_button2 = tk.Button(frame3, bg="darkgray", width=5, height=1, text="2", font="Impact", command=self.neutral_button_2)
        self.neutral_button3 = tk.Button(frame3, bg="darkgray", width=5, height=1, text="3", font="Impact", command=self.neutral_button_3)
        self.neutral_button4 = tk.Button(frame3, bg="darkgray", width=5, height=1, text="4", font="Impact", command=self.neutral_button_4)
        self.neutral_button5 = tk.Button(frame3, bg="darkgray", width=5, height=1, text="5", font="Impact", command=self.neutral_button_5)

        darkblue_button = tk.Button(frame4, bg="darkblue", width= default_width_colors, height= default_height_colors, command=self.darkblue_button_function)
        lightgreen_button = tk.Button(frame4, bg="lightgreen", width= default_width_colors, height= default_height_colors, command=self.lightgreen_button_function)
        lightblue_button = tk.Button(frame4, bg="lightblue", width= default_width_colors, height= default_height_colors, command=self.lightblue_button_function)

        blueblack_button = tk.Button(frame5, bg="#000555", width= default_width_colors, height= default_height_colors, command=self.blueblack_button_function)
        darkgreen_button = tk.Button(frame5, bg="darkgreen", width= default_width_colors, height= default_height_colors, command=self.darkgreen_button_function)
        lightbrown_button = tk.Button(frame5, bg="#ccb894", width= default_width_colors, height= default_height_colors, command=self.lightbrown_button_function)
        
        darkred_button = tk.Button(frame6, bg="#bb0000", width= default_width_colors, height= default_height_colors, command=self.darkred_button_function)
        clearblue_button = tk.Button(frame6, bg="#33bbff", width= default_width_colors, height= default_height_colors, command=self.clearblue_button_function)
        goldmetal_button = tk.Button(frame6, bg="#a19000", width= default_width_colors, height= default_height_colors, command=self.goldmetal_button_function)
        self.start_game_button = tk.Button(frame6, bg="green", fg="white", text="START", command=self.start_game)
        self.verify_button = tk.Button(frame6, bg="gray", fg="white", text="VERIFY", command=self.verify_button_function)

        self.tries_score_text = tk.Label(frame7, text=f"Tries this round: {self.tries_this_round}", bg="lightgray")
        self.rounds_score_text = tk.Label(frame7, text=f"Rounds played in total: {self.rounds_played}", bg="lightgray")
        self.wins_score_text = tk.Label(frame7, text=f"Wins in total: {self.num_of_wins}", bg="lightgray")

        # Packs

        frame1.pack(anchor="e", padx=5, pady=(5,0))
        self.status_text.pack(side=tk.LEFT, padx= 55)
        black_button.pack(side=tk.LEFT, padx=1, pady=1)
        red_button.pack(side=tk.LEFT, padx=1, pady=1)
        yellow_button.pack(side=tk.LEFT, padx=1, pady=1)

        frame2.pack(anchor="e", padx=5)
        blue_button.pack(side=tk.LEFT, padx=1, pady=1)
        green_button.pack(side=tk.LEFT, padx=1, pady=1)
        pink_button.pack(side=tk.LEFT, padx=1, pady=1)

        frame3.pack(anchor="e", padx=5)
        self.neutral_button1.pack(side=tk.LEFT, padx=1)
        self.neutral_button2.pack(side=tk.LEFT, padx=1)
        self.neutral_button3.pack(side=tk.LEFT, padx=1)
        self.neutral_button4.pack(side=tk.LEFT, padx=1)
        self.neutral_button5.pack(side=tk.LEFT, padx=(1,40))
        orange_button.pack(side=tk.LEFT, padx=1, pady=1)
        purple_button.pack(side=tk.LEFT, padx=1, pady=1)
        cyan_button.pack(side=tk.LEFT, padx=1, pady=1)

        frame4.pack(anchor="e", padx=5)
        darkblue_button.pack(side=tk.LEFT, padx=1, pady=1)
        lightgreen_button.pack(side=tk.LEFT, padx=1, pady=1)
        lightblue_button.pack(side=tk.LEFT, padx=1, pady=1)

        frame5.pack(anchor="e", padx=5)
        blueblack_button.pack(side=tk.LEFT, padx=1, pady=1)
        darkgreen_button.pack(side=tk.LEFT, padx=1, pady=1)
        lightbrown_button.pack(side=tk.LEFT, padx=1, pady=1)

        frame6.pack(anchor="e", padx=5)
        self.verify_button.pack(side=tk.LEFT, padx=11)
        self.start_game_button.pack(side=tk.LEFT, padx=(0,55))
        darkred_button.pack(side=tk.LEFT, padx=1, pady=1)
        clearblue_button.pack(side=tk.LEFT, padx=1, pady=1)
        goldmetal_button.pack(side=tk.LEFT, padx=1, pady=1)

        frame7.pack(padx=5,pady=11)
        self.tries_score_text.pack(side=tk.RIGHT,padx=1)
        self.rounds_score_text.pack(side=tk.RIGHT,padx=1)
        self.wins_score_text.pack(side=tk.RIGHT,padx=1)

    def start_game(self):
        if not self.game_started:
            self.game_started = True
            self.colors_choosed_by_calculator = random.choices(self.all_colors, k=5)
            self.can_the_player_choose_a_num = True
            self.status_text.config(text='The game has started, choose a num to modify')
            self.start_game_button.config(text="STOP", bg="red")
        else:
            self.game_started = False
            self.can_the_player_choose_a_num = False
            self.status_text.config(text='The game has not started yet')
            self.start_game_button.config(text="START", bg="green")
            self.neutral_button1.config(bg="darkgray")
            self.neutral_button2.config(bg="darkgray")
            self.neutral_button3.config(bg="darkgray")
            self.neutral_button4.config(bg="darkgray")
            self.neutral_button5.config(bg="darkgray")
            self.colors_choosed_by_user = ["?", "?", "?", "?", "?"]
            self.can_verify = False
            self.on_modify_index = -1
            self.can_the_player_choose_a_color = False
            self.rounds_played += 1
            self.colors_choosed_by_calculator.clear()
            self.tries_this_round = 0
            self.tries_score_text.config(text=f"Tries this round: {self.tries_this_round}")
            self.rounds_score_text.config(text=f"Rounds played in total: {self.rounds_played}")
            
        if "?" in self.colors_choosed_by_user:
            self.can_verify = False
            self.verify_button.config(bg="gray")

    def verify_button_function(self):
        a = 0
        correct_colors = 0
        if self.can_verify:
            for i in self.colors_choosed_by_user:
                if i == self.colors_choosed_by_calculator[a]:
                    correct_colors += 1
                a += 1
            a = 0
        self.status_text.config(text=f'You have {correct_colors} correct colors')
        self.tries_this_round += 1
        self.tries_score_text.config(text=f"Tries this round: {self.tries_this_round}")
        if correct_colors == 5:
            winner = True
            if winner:
                self.status_text.config(text='Good job, you win! GAME OVER')
                self.num_of_wins += 1
                winner = False
                self.wins_score_text.config(text=f"Wins in total: {self.num_of_wins}")
                self.after(5000, self.start_game)

    def neutral_button_1(self):
        if self.can_the_player_choose_a_num:
            self.on_modify_index = 0
            self.status_text.config(text='You are modifying the color 1, now select a color')
            self.can_the_player_choose_a_color = True
            if self.on_modify_index in range(0,5):
                self.has_selected_a_num = True
        elif not self.can_the_player_choose_a_color and not self.game_started:
            self.status_text.config(text='You can only modify a choice when the game has started')
    
    def neutral_button_2(self):
        if self.can_the_player_choose_a_num:
            self.on_modify_index = 1
            self.status_text.config(text='You are modifying the color 2, now select a color')
            self.can_the_player_choose_a_color = True
        elif not self.can_the_player_choose_a_color and not self.game_started:
            self.status_text.config(text='You can only modify a choice when the game has started')

    def neutral_button_3(self):
        if self.can_the_player_choose_a_num:
            self.on_modify_index = 2
            self.status_text.config(text='You are modifying the color 3, now select a color')
            self.can_the_player_choose_a_color = True
        elif not self.can_the_player_choose_a_color and not self.game_started:
            self.status_text.config(text='You can only modify a choice when the game has started')
    
    def neutral_button_4(self):
        if self.can_the_player_choose_a_num:
            self.on_modify_index = 3
            self.status_text.config(text='You are modifying the color 4, now select a color')
            self.can_the_player_choose_a_color = True
        elif not self.can_the_player_choose_a_color and not self.game_started:
            self.status_text.config(text='You can only modify a choice when the game has started')
    
    def neutral_button_5(self):
        if self.can_the_player_choose_a_num:
            self.on_modify_index = 4
            self.status_text.config(text='You are modifying the color 5, now select a color')
            self.can_the_player_choose_a_color = True
        elif not self.can_the_player_choose_a_color and not self.game_started:
            self.status_text.config(text='You can only modify a choice when the game has started')
    
    def black_button_function(self):
        if self.can_the_player_choose_a_color:
            self.colors_choosed_by_user[self.on_modify_index] = "black"
            self.status_text.config(text=f'Button {self.on_modify_index + 1} has been modified in black')
            self.can_the_player_choose_a_color = False

            if self.on_modify_index == 0:
                self.neutral_button1.config(bg="black")
            elif self.on_modify_index == 1:
                self.neutral_button2.config(bg="black")
            elif self.on_modify_index == 2:
                self.neutral_button3.config(bg="black")
            elif self.on_modify_index == 3:
                self.neutral_button4.config(bg="black")
            elif self.on_modify_index == 4:
                self.neutral_button5.config(bg="black")

        elif not self.has_selected_a_num and self.game_started:
            self.status_text.config(text='You must select a neutral button to modify first')

        elif not self.has_selected_a_num and not self.game_started:
            self.status_text.config(text='You must start the game first')
        
        self.has_selected_a_num = False

        if not "?" in self.colors_choosed_by_user:
            self.can_verify = True
            self.verify_button.config(bg="blue")
    
    def red_button_function(self):
        if self.can_the_player_choose_a_color:
            self.colors_choosed_by_user[self.on_modify_index] = "red"
            self.status_text.config(text=f'Button {self.on_modify_index + 1} has been modified in red')
            self.can_the_player_choose_a_color = False

            if self.on_modify_index == 0:
                self.neutral_button1.config(bg="red")
            elif self.on_modify_index == 1:
                self.neutral_button2.config(bg="red")
            elif self.on_modify_index == 2:
                self.neutral_button3.config(bg="red")
            elif self.on_modify_index == 3:
                self.neutral_button4.config(bg="red")
            elif self.on_modify_index == 4:
                self.neutral_button5.config(bg="red")

        elif not self.has_selected_a_num and self.game_started:
            self.status_text.config(text='You must select a neutral button to modify first')

        elif not self.has_selected_a_num and not self.game_started:
            self.status_text.config(text='You must start the game first')

        self.has_selected_a_num = False

        if not "?" in self.colors_choosed_by_user:
            self.can_verify = True
            self.verify_button.config(bg="blue")

    def yellow_button_function(self):
        if self.can_the_player_choose_a_color:
            self.colors_choosed_by_user[self.on_modify_index] = "yellow"
            self.status_text.config(text=f'Button {self.on_modify_index + 1} has been modified in yellow')
            self.can_the_player_choose_a_color = False

            if self.on_modify_index == 0:
                self.neutral_button1.config(bg="yellow")
            elif self.on_modify_index == 1:
                self.neutral_button2.config(bg="yellow")
            elif self.on_modify_index == 2:
                self.neutral_button3.config(bg="yellow")
            elif self.on_modify_index == 3:
                self.neutral_button4.config(bg="yellow")
            elif self.on_modify_index == 4:
                self.neutral_button5.config(bg="yellow")

        elif not self.has_selected_a_num and self.game_started:
            self.status_text.config(text='You must select a neutral button to modify first')

        elif not self.has_selected_a_num and not self.game_started:
            self.status_text.config(text='You must start the game first')

        self.has_selected_a_num = False

        if not "?" in self.colors_choosed_by_user:
            self.can_verify = True
            self.verify_button.config(bg="blue")
        
    def blue_button_function(self):
        if self.can_the_player_choose_a_color:
            self.colors_choosed_by_user[self.on_modify_index] = "blue"
            self.status_text.config(text=f'Button {self.on_modify_index + 1} has been modified in blue')
            self.can_the_player_choose_a_color = False

            if self.on_modify_index == 0:
                self.neutral_button1.config(bg="blue")
            elif self.on_modify_index == 1:
                self.neutral_button2.config(bg="blue")
            elif self.on_modify_index == 2:
                self.neutral_button3.config(bg="blue")
            elif self.on_modify_index == 3:
                self.neutral_button4.config(bg="blue")
            elif self.on_modify_index == 4:
                self.neutral_button5.config(bg="blue")

        elif not self.has_selected_a_num and self.game_started:
            self.status_text.config(text='You must select a neutral button to modify first')

        elif not self.has_selected_a_num and not self.game_started:
            self.status_text.config(text='You must start the game first')

        self.has_selected_a_num = False

        if not "?" in self.colors_choosed_by_user:
            self.can_verify = True
            self.verify_button.config(bg="blue")

    def green_button_function(self):
        if self.can_the_player_choose_a_color:
            self.colors_choosed_by_user[self.on_modify_index] = "green"
            self.status_text.config(text=f'Button {self.on_modify_index + 1} has been modified in green')
            self.can_the_player_choose_a_color = False

            if self.on_modify_index == 0:
                self.neutral_button1.config(bg="green")
            elif self.on_modify_index == 1:
                self.neutral_button2.config(bg="green")
            elif self.on_modify_index == 2:
                self.neutral_button3.config(bg="green")
            elif self.on_modify_index == 3:
                self.neutral_button4.config(bg="green")
            elif self.on_modify_index == 4:
                self.neutral_button5.config(bg="green")

        elif not self.has_selected_a_num and self.game_started:
            self.status_text.config(text='You must select a neutral button to modify first')

        elif not self.has_selected_a_num and not self.game_started:
            self.status_text.config(text='You must start the game first')

        self.has_selected_a_num = False

        if not "?" in self.colors_choosed_by_user:
            self.can_verify = True
            self.verify_button.config(bg="blue")

    def pink_button_function(self):
        if self.can_the_player_choose_a_color:
            self.colors_choosed_by_user[self.on_modify_index] = "pink"
            self.status_text.config(text=f'Button {self.on_modify_index + 1} has been modified in pink')
            self.can_the_player_choose_a_color = False

            if self.on_modify_index == 0:
                self.neutral_button1.config(bg="pink")
            elif self.on_modify_index == 1:
                self.neutral_button2.config(bg="pink")
            elif self.on_modify_index == 2:
                self.neutral_button3.config(bg="pink")
            elif self.on_modify_index == 3:
                self.neutral_button4.config(bg="pink")
            elif self.on_modify_index == 4:
                self.neutral_button5.config(bg="pink")

        elif not self.has_selected_a_num and self.game_started:
            self.status_text.config(text='You must select a neutral button to modify first')

        elif not self.has_selected_a_num and not self.game_started:
            self.status_text.config(text='You must start the game first')

        self.has_selected_a_num = False

        if not "?" in self.colors_choosed_by_user:
            self.can_verify = True
            self.verify_button.config(bg="blue")

    def orange_button_function(self):
        if self.can_the_player_choose_a_color:
            self.colors_choosed_by_user[self.on_modify_index] = "orange"
            self.status_text.config(text=f'Button {self.on_modify_index + 1} has been modified in orange')
            self.can_the_player_choose_a_color = False

            if self.on_modify_index == 0:
                self.neutral_button1.config(bg="orange")
            elif self.on_modify_index == 1:
                self.neutral_button2.config(bg="orange")
            elif self.on_modify_index == 2:
                self.neutral_button3.config(bg="orange")
            elif self.on_modify_index == 3:
                self.neutral_button4.config(bg="orange")
            elif self.on_modify_index == 4:
                self.neutral_button5.config(bg="orange")

        elif not self.has_selected_a_num and self.game_started:
            self.status_text.config(text='You must select a neutral button to modify first')

        elif not self.has_selected_a_num and not self.game_started:
            self.status_text.config(text='You must start the game first')

        self.has_selected_a_num = False

        if not "?" in self.colors_choosed_by_user:
            self.can_verify = True
            self.verify_button.config(bg="blue")

    def purple_button_function(self):
        if self.can_the_player_choose_a_color:
            self.colors_choosed_by_user[self.on_modify_index] = "purple"
            self.status_text.config(text=f'Button {self.on_modify_index + 1} has been modified in purple')
            self.can_the_player_choose_a_color = False

            if self.on_modify_index == 0:
                self.neutral_button1.config(bg="purple")
            elif self.on_modify_index == 1:
                self.neutral_button2.config(bg="purple")
            elif self.on_modify_index == 2:
                self.neutral_button3.config(bg="purple")
            elif self.on_modify_index == 3:
                self.neutral_button4.config(bg="purple")
            elif self.on_modify_index == 4:
                self.neutral_button5.config(bg="purple")

        elif not self.has_selected_a_num and self.game_started:
            self.status_text.config(text='You must select a neutral button to modify first')

        elif not self.has_selected_a_num and not self.game_started:
            self.status_text.config(text='You must start the game first')

        self.has_selected_a_num = False

        if not "?" in self.colors_choosed_by_user:
            self.can_verify = True
            self.verify_button.config(bg="blue")

    def cyan_button_function(self):
        if self.can_the_player_choose_a_color:
            self.colors_choosed_by_user[self.on_modify_index] = "cyan"
            self.status_text.config(text=f'Button {self.on_modify_index + 1} has been modified in cyan')
            self.can_the_player_choose_a_color = False

            if self.on_modify_index == 0:
                self.neutral_button1.config(bg="cyan")
            elif self.on_modify_index == 1:
                self.neutral_button2.config(bg="cyan")
            elif self.on_modify_index == 2:
                self.neutral_button3.config(bg="cyan")
            elif self.on_modify_index == 3:
                self.neutral_button4.config(bg="cyan")
            elif self.on_modify_index == 4:
                self.neutral_button5.config(bg="cyan")

        elif not self.has_selected_a_num and self.game_started:
            self.status_text.config(text='You must select a neutral button to modify first')

        elif not self.has_selected_a_num and not self.game_started:
            self.status_text.config(text='You must start the game first')

        self.has_selected_a_num = False

        if not "?" in self.colors_choosed_by_user:
            self.can_verify = True
            self.verify_button.config(bg="blue")

    def darkblue_button_function(self):
        if self.can_the_player_choose_a_color:
            self.colors_choosed_by_user[self.on_modify_index] = "darkblue"
            self.status_text.config(text=f'Button {self.on_modify_index + 1} has been modified in darkblue')
            self.can_the_player_choose_a_color = False

            if self.on_modify_index == 0:
                self.neutral_button1.config(bg="darkblue")
            elif self.on_modify_index == 1:
                self.neutral_button2.config(bg="darkblue")
            elif self.on_modify_index == 2:
                self.neutral_button3.config(bg="darkblue")
            elif self.on_modify_index == 3:
                self.neutral_button4.config(bg="darkblue")
            elif self.on_modify_index == 4:
                self.neutral_button5.config(bg="darkblue")

        elif not self.has_selected_a_num and self.game_started:
            self.status_text.config(text='You must select a neutral button to modify first')

        elif not self.has_selected_a_num and not self.game_started:
            self.status_text.config(text='You must start the game first')

        self.has_selected_a_num = False

        if not "?" in self.colors_choosed_by_user:
            self.can_verify = True
            self.verify_button.config(bg="blue")

    def lightgreen_button_function(self):
        if self.can_the_player_choose_a_color:
            self.colors_choosed_by_user[self.on_modify_index] = "lightgreen"
            self.status_text.config(text=f'Button {self.on_modify_index + 1} has been modified in lightgreen')
            self.can_the_player_choose_a_color = False

            if self.on_modify_index == 0:
                self.neutral_button1.config(bg="lightgreen")
            elif self.on_modify_index == 1:
                self.neutral_button2.config(bg="lightgreen")
            elif self.on_modify_index == 2:
                self.neutral_button3.config(bg="lightgreen")
            elif self.on_modify_index == 3:
                self.neutral_button4.config(bg="lightgreen")
            elif self.on_modify_index == 4:
                self.neutral_button5.config(bg="lightgreen")

        elif not self.has_selected_a_num and self.game_started:
            self.status_text.config(text='You must select a neutral button to modify first')

        elif not self.has_selected_a_num and not self.game_started:
            self.status_text.config(text='You must start the game first')

        self.has_selected_a_num = False

        if not "?" in self.colors_choosed_by_user:
            self.can_verify = True
            self.verify_button.config(bg="blue")

    def lightblue_button_function(self):
        if self.can_the_player_choose_a_color:
            self.colors_choosed_by_user[self.on_modify_index] = "lightblue"
            self.status_text.config(text=f'Button {self.on_modify_index + 1} has been modified in lightblue')
            self.can_the_player_choose_a_color = False

            if self.on_modify_index == 0:
                self.neutral_button1.config(bg="lightblue")
            elif self.on_modify_index == 1:
                self.neutral_button2.config(bg="lightblue")
            elif self.on_modify_index == 2:
                self.neutral_button3.config(bg="lightblue")
            elif self.on_modify_index == 3:
                self.neutral_button4.config(bg="lightblue")
            elif self.on_modify_index == 4:
                self.neutral_button5.config(bg="lightblue")

        elif not self.has_selected_a_num and self.game_started:
            self.status_text.config(text='You must select a neutral button to modify first')

        elif not self.has_selected_a_num and not self.game_started:
            self.status_text.config(text='You must start the game first')

        self.has_selected_a_num = False

        if not "?" in self.colors_choosed_by_user:
            self.can_verify = True
            self.verify_button.config(bg="blue")

    def blueblack_button_function(self):
        if self.can_the_player_choose_a_color:
            self.colors_choosed_by_user[self.on_modify_index] = "blueblack"
            self.status_text.config(text=f'Button {self.on_modify_index + 1} has been modified in blueblack')
            self.can_the_player_choose_a_color = False

            if self.on_modify_index == 0:
                self.neutral_button1.config(bg="#000555")
            elif self.on_modify_index == 1:
                self.neutral_button2.config(bg="#000555")
            elif self.on_modify_index == 2:
                self.neutral_button3.config(bg="#000555")
            elif self.on_modify_index == 3:
                self.neutral_button4.config(bg="#000555")
            elif self.on_modify_index == 4:
                self.neutral_button5.config(bg="#000555")

        elif not self.has_selected_a_num and self.game_started:
            self.status_text.config(text='You must select a neutral button to modify first')

        elif not self.has_selected_a_num and not self.game_started:
            self.status_text.config(text='You must start the game first')

        self.has_selected_a_num = False

        if not "?" in self.colors_choosed_by_user:
            self.can_verify = True
            self.verify_button.config(bg="blue")

    def darkgreen_button_function(self):
        if self.can_the_player_choose_a_color:
            self.colors_choosed_by_user[self.on_modify_index] = "darkgreen"
            self.status_text.config(text=f'Button {self.on_modify_index + 1} has been modified in darkgreen')
            self.can_the_player_choose_a_color = False

            if self.on_modify_index == 0:
                self.neutral_button1.config(bg="darkgreen")
            elif self.on_modify_index == 1:
                self.neutral_button2.config(bg="darkgreen")
            elif self.on_modify_index == 2:
                self.neutral_button3.config(bg="darkgreen")
            elif self.on_modify_index == 3:
                self.neutral_button4.config(bg="darkgreen")
            elif self.on_modify_index == 4:
                self.neutral_button5.config(bg="darkgreen")

        elif not self.has_selected_a_num and self.game_started:
            self.status_text.config(text='You must select a neutral button to modify first')

        elif not self.has_selected_a_num and not self.game_started:
            self.status_text.config(text='You must start the game first')

        self.has_selected_a_num = False

        if not "?" in self.colors_choosed_by_user:
            self.can_verify = True
            self.verify_button.config(bg="blue")

    def lightbrown_button_function(self):
        if self.can_the_player_choose_a_color:
            self.colors_choosed_by_user[self.on_modify_index] = "lightbrown"
            self.status_text.config(text=f'Button {self.on_modify_index + 1} has been modified in lightbrown')
            self.can_the_player_choose_a_color = False

            if self.on_modify_index == 0:
                self.neutral_button1.config(bg="#ccb894")
            elif self.on_modify_index == 1:
                self.neutral_button2.config(bg="#ccb894")
            elif self.on_modify_index == 2:
                self.neutral_button3.config(bg="#ccb894")
            elif self.on_modify_index == 3:
                self.neutral_button4.config(bg="#ccb894")
            elif self.on_modify_index == 4:
                self.neutral_button5.config(bg="#ccb894")

        elif not self.has_selected_a_num and self.game_started:
            self.status_text.config(text='You must select a neutral button to modify first')

        elif not self.has_selected_a_num and not self.game_started:
            self.status_text.config(text='You must start the game first')

        self.has_selected_a_num = False

        if not "?" in self.colors_choosed_by_user:
            self.can_verify = True
            self.verify_button.config(bg="blue")

    def darkred_button_function(self):
        if self.can_the_player_choose_a_color:
            self.colors_choosed_by_user[self.on_modify_index] = "darkred"
            self.status_text.config(text=f'Button {self.on_modify_index + 1} has been modified in darkred')
            self.can_the_player_choose_a_color = False

            if self.on_modify_index == 0:
                self.neutral_button1.config(bg="#bb0000")
            elif self.on_modify_index == 1:
                self.neutral_button2.config(bg="#bb0000")
            elif self.on_modify_index == 2:
                self.neutral_button3.config(bg="#bb0000")
            elif self.on_modify_index == 3:
                self.neutral_button4.config(bg="#bb0000")
            elif self.on_modify_index == 4:
                self.neutral_button5.config(bg="#bb0000")

        elif not self.has_selected_a_num and self.game_started:
            self.status_text.config(text='You must select a neutral button to modify first')

        elif not self.has_selected_a_num and not self.game_started:
            self.status_text.config(text='You must start the game first')

        self.has_selected_a_num = False

        if not "?" in self.colors_choosed_by_user:
            self.can_verify = True
            self.verify_button.config(bg="blue")

    def clearblue_button_function(self):
        if self.can_the_player_choose_a_color:
            self.colors_choosed_by_user[self.on_modify_index] = "clearblue"
            self.status_text.config(text=f'Button {self.on_modify_index + 1} has been modified in clearblue')
            self.can_the_player_choose_a_color = False

            if self.on_modify_index == 0:
                self.neutral_button1.config(bg="#33bbff")
            elif self.on_modify_index == 1:
                self.neutral_button2.config(bg="#33bbff")
            elif self.on_modify_index == 2:
                self.neutral_button3.config(bg="#33bbff")
            elif self.on_modify_index == 3:
                self.neutral_button4.config(bg="#33bbff")
            elif self.on_modify_index == 4:
                self.neutral_button5.config(bg="#33bbff")

        elif not self.has_selected_a_num and self.game_started:
            self.status_text.config(text='You must select a neutral button to modify first')

        elif not self.has_selected_a_num and not self.game_started:
            self.status_text.config(text='You must start the game first')

        self.has_selected_a_num = False

        if not "?" in self.colors_choosed_by_user:
            self.can_verify = True
            self.verify_button.config(bg="blue")

    def goldmetal_button_function(self):
        if self.can_the_player_choose_a_color:
            self.colors_choosed_by_user[self.on_modify_index] = "goldmetal"
            self.status_text.config(text=f'Button {self.on_modify_index + 1} has been modified in goldmetal')
            self.can_the_player_choose_a_color = False

            if self.on_modify_index == 0:
                self.neutral_button1.config(bg="#a19000")
            elif self.on_modify_index == 1:
                self.neutral_button2.config(bg="#a19000")
            elif self.on_modify_index == 2:
                self.neutral_button3.config(bg="#a19000")
            elif self.on_modify_index == 3:
                self.neutral_button4.config(bg="#a19000")
            elif self.on_modify_index == 4:
                self.neutral_button5.config(bg="#a19000")

        elif not self.has_selected_a_num and self.game_started:
            self.status_text.config(text='You must select a neutral button to modify first')

        elif not self.has_selected_a_num and not self.game_started:
            self.status_text.config(text='You must start the game first')

        self.has_selected_a_num = False

        if not "?" in self.colors_choosed_by_user:
            self.can_verify = True
            self.verify_button.config(bg="blue")

window = App()
window.mainloop()