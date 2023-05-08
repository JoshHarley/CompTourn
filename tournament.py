from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import RoundRobin

class Player:
    def __init__(self, name, villain = "", score = 0, villains_played = []):
        self.name = name
        self.villain = villain
        self.score = score    
        self.villains_played = villains_played

class Villain:
    def __init__(self, name, score = 0):
        self.name = name
        self.score = score

villainsList = ["Scar", "Hades", "Captain Hook", "Jafar", "Maleficent", "Prince John", "Queen of Hearts", "Ursula", "Dr. Facilier", "Evil Queen", "Ratigan", "Yzma"]
villains = []
villains_updated = []
player_assigned_villains = []
players = []
player_entry_entries = []
number_of_players = None
number_of_villains = None
villain_to_be_assigned = []
round_num = 1

for villain in villainsList:
    villains.append(Villain(villain))

def handle_enter(event):
    if frame.focus_get() == submit_button:
        number_entry(player_number_get.get(), villain_number_get.get())
    elif frame2.focus_get() == submit_button_2:
        update_player_list()
    elif frame2.focus_get() == back_button:
        go_back()
    elif frame2.focus_get() == round_result_button:
        next_round()

def assign_villain():
    global villain_to_be_assigned, player_assigned_villains, villains_updated
    assigned_villain = random.choice(villains_updated)
    if assigned_villain not in player_assigned_villains:
        player_assigned_villains.append(assigned_villain)
        villain_to_be_assigned.append(assigned_villain)
    else:
        assign_villain()

def player_setup():
    global players, villains_updated, player_assigned_villains, round_num
    for player in players:  
        assign_villain()
        if villain_to_be_assigned not in player.villains_played and villain_to_be_assigned[0] in player_assigned_villains:
            player.villain = villain_to_be_assigned[0]
            player.villains_played += villain_to_be_assigned
            villain_to_be_assigned.clear()
        else:
            player_setup()
    player_assigned_villains.clear()
    

def number_entry(player_num, villain_num):
    # Function to retrieve user input for number of players, save it in a global variable and display it.
    global number_of_players, number_of_villains, villains
    try:
        number_of_players = int(player_num)
        number_of_villains = int(villain_num)
    except ValueError:
        messagebox.showerror(title = "Not A Number", message = "Value entered is not a number")
    for v in range(0, number_of_players):
        assigned_villain = random.choice(villains)
        villains_updated.append(assigned_villain)
    arrange_frame_2(number_of_players)
    frame2.tkraise()

def number_validation(number):
    try:
        if number.isdigit() and int(number) < 5:
            return True
    except:
        player_number_get_entry.focus()
        return False
    return False

def player_name_validation(letter):
    try:
        if not str.isdigit(letter):
            return True
    except:
        frame2.entry.focus()
        frame2.entry.delete(0, END)
        return False
    return False

def go_back():
    frame.tkraise()
    player_entry_entries.clear()
    frame2.grid_forget()

def arrange_frame_2(number):
    global players, player_entry_entries
    player_name_check = (frame2.register(player_name_validation))
    last_row = 2
    for i in range(1, number + 1):
        Label(frame2, text = f"Player {i} name: ").grid(column = 1, row = 1 + i)
        frame2.rowconfigure(i, weight=1)
        last_row += 1
        letter = StringVar()
        entry = Entry(frame2, width = 7, textvariable = letter, validate = 'key', validatecommand = (player_name_check, '%S'))
        entry.grid(column = 2, row = i + 1, sticky = (W, E))
        player_entry_entries.append(entry)  
    player_entry_entries[0].focus()
    submit_button_2.grid(column = 1, row = last_row, sticky = (W, S, N, E))
    back_button.grid(column = 2, row = last_row, sticky = (W, S, N, E))

def arrange_frame_3(round):
    global round_num
    i = 1
    Label(frame3, text = f'Round {round}').grid(row = 0, column = 1, sticky = (W), columnspan = 3)
    for player in players:
        Label(frame3, text = "Player").grid(row = i, column = 1, sticky = (W))
        Label(frame3, text = player.name).grid(row = i, column = 2, sticky = (W))
        Label(frame3, text = player.villain.name).grid(row = i, column = 3, sticky = (W))
        i += 1
    round_result_button = Button(frame3, width = 7, text = "Next Round", command = round_result)
    round_result_button.grid(row = i + 1, column = 1, columnspan = 3, sticky = (W, E, N, S))
    round_num += 1

def round_result():
    if round_num > len(villains_updated):
        for widget in frame3.winfo_children():
            widget.destroy()
            player_name_check = (frame3.register(player_name_validation))
            frame3.rowconfigure(1, weight=1)
            frame3.rowconfigure(2, weight=1)
            frame3.columnconfigure(1, weight=1)
            frame3.columnconfigure(2, weight=1)
            Label(frame3, text = f"Enter the winner of round {round_num - 1}").grid(row = 1, column = 1)
            winner = StringVar()
            winner_entry = Entry(frame3, textvariable = winner, validate = 'key', validatecommand = (player_name_check, '%S'))
            winner_entry.grid(row = 1, column = 2)
            next_round_button = Button(frame3, width = 7, text = "End Game", command = lambda: final_result(winner_entry.get()))
            next_round_button.grid(row = 2, column = 1, columnspan = 2, sticky = (W, E, N, S))
    else:
        for widget in frame3.winfo_children():
            widget.destroy()
            player_name_check = (frame3.register(player_name_validation))
            frame3.rowconfigure(1, weight=1)
            frame3.rowconfigure(2, weight=1)
            frame3.columnconfigure(1, weight=1)
            frame3.columnconfigure(2, weight=1)
            Label(frame3, text = f"Enter the winner of round {round_num - 1}").grid(row = 1, column = 1)
            winner = StringVar()
            winner_entry = Entry(frame3, textvariable = winner, validate = 'key', validatecommand = (player_name_check, '%S'))
            winner_entry.grid(row = 1, column = 2)
            next_round_button = Button(frame3, width = 7, text = "Next Round", command = lambda: next_round(winner_entry.get()))
            next_round_button.grid(row = 2, column = 1, columnspan = 2, sticky = (W, E, N, S))
    
def final_result(result):
    global players, villains_updated
    pr = 2
    vr = 1
    RoundRobin.updateScore(result, players, villains_updated)
    for widget in frame3.winfo_children():
        widget.destroy()
    Label(frame3, text = "Final Results: ").grid(row = 1, column = 1)
    players.sort(key = lambda players: players.score, reverse = True)
    villains_updated.sort(key = lambda villains: villains.score, reverse = True)
    for player in players:
        Label(frame3, text = f'{pr - 1}').grid(row = pr, column = 1)
        Label(frame3, text = "Player Name: ").grid(row = pr, column = 2)
        Label(frame3, text = f"{player.name}").grid(row = pr, column = 3)
        Label(frame3, text = "Score: ").grid(row = pr, column = 4)
        Label(frame3, text = f"{player.score}").grid(row = pr, column = 5)
        pr += 1    
    Label(frame3, text = "Villain Scores: ").grid(row = pr, column = 1)
    pr += 1
    for villain in villains_updated:
        Label(frame3, text = f'{vr}').grid(row = pr, column = 1)
        Label(frame3, text = "Villain Name: ").grid(row = pr, column = 2)
        Label(frame3, text = f"{villain.name}").grid(row = pr, column = 3)
        Label(frame3, text = "Score: ").grid(row = pr, column = 4)
        Label(frame3, text = f"{villain.score}").grid(row = pr, column = 5)
        vr += 1
        pr += 1


def next_round(result):
    global players, villains_updated
    RoundRobin.updateScore(result, players, villains_updated)
    player_setup()
    for widget in frame3.winfo_children():
       widget.destroy()
    arrange_frame_3(round_num)

def update_player_list():
    global players, player_entry_entries, round_num
    name_valid = False
    for entry in player_entry_entries:
        if (len(entry.get()) > 9 or len(entry.get()) < 1):
            name_valid = True
    if name_valid:
        messagebox.showerror(title = "Input invalid", message = "Input entered was greater than 9 letters long or empty")
    else:
        for entry in player_entry_entries:  
            name = entry.get()
            players.append(Player(name))
    
    player_setup()
    arrange_frame_3(f'Round {round_num}')
    frame3.tkraise()



root = Tk()
root.title("Villainous Tournament")
root.rowconfigure(0, weight = 1)
root.columnconfigure(0, weight = 1)
root.bind('<Return>', handle_enter)

frame = ttk.Frame(root, padding = "3 3 12 12", height = 100, width = 100)
frame.grid(column = 0, row = 0, sticky = (W, S, N, E))
frame.rowconfigure(1, weight=1)
frame.rowconfigure(2, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)
number_check = (frame.register(number_validation))

player_number_get = StringVar()
player_number_get_entry = Entry(frame, width = 10, textvariable = player_number_get, validate = "key", validatecommand = (number_check, '%S'))
player_number_get_entry.grid(column = 2, row = 2, sticky= (W, E))
ttk.Label(frame, text = "Enter the number of players: ").grid(column = 1, row = 2, sticky= (W, E))
villain_number_get = StringVar()
villain_number_get_entry = Entry(frame, width = 10, textvariable = villain_number_get, validate = "key", validatecommand = (number_check, '%S'))
villain_number_get_entry.grid(column = 2, row = 3, sticky= (W, E))
ttk.Label(frame, text = "Enter the number of villain: ").grid(column = 1, row = 3, sticky= (W, E))
player_number_get_entry.focus()

submit_button = Button(frame, width = 7, text = "Submit", command = lambda: number_entry(player_number_get.get(), villain_number_get.get()))
submit_button.grid(column = 1, row = 4, columnspan = 2, sticky = (W, S, N, E))

frame2 = ttk.Frame(root, padding = "3 3 12 12")
frame2.grid(column = 0, row = 0, sticky = (W, S, N, E))
frame2.columnconfigure(1, weight=1)
frame2.columnconfigure(2, weight=1)
submit_button_2 = Button(frame2, width = 7, text = "Submit", command = update_player_list)
back_button = Button(frame2, width = 7, text = "Back", command = go_back)

frame3 = ttk.Frame(root, padding = "3 3 12 12")
frame3.grid(column = 0, row = 0, sticky = (W, S, N, E))
frame3.rowconfigure(1, weight=1)
frame3.rowconfigure(2, weight=1)
frame3.columnconfigure(1, weight=1)
frame3.columnconfigure(2, weight=1)

ttk.Label(frame2, text = "Enter the player names: ").grid(column = 1, row = 1, sticky = (W, S, N, E))

frame.tkraise()
root.update()
root.mainloop()