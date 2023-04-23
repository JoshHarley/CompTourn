from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

class Player:
    def __init__(self, name, villain, score = 0, villains_played = []):
        self.name = name
        self.villain = villain
        self.score = score    
        self.villains = villains_played

villains = ["Scar", "Hades", "Captain Hook", "Jafar", "Maleficent", "Prince John", "Queen of Hearts", "Ursula", "Dr. Facilier", "Evil Queen", "Ratigan", "Yzma"]

villains_updated = []

players = []

player_entry_entries = []

number_of_players = None

number_of_villains = None

def handle_enter(event):
    if frame.focus_get() == submit_button:
        number_entry(player_number_get.get(), villain_number_get.get())
    elif frame2.focus_get() == submit_button_2:
        update_player()
    elif frame2.focus_get() == back_button:
        go_back()
    elif frame2.focus_get() == next_round_button:
        next_round()

def assign_villain():
    assigned_villain = random.choice(villains_updated)
    villains_updated.remove(assigned_villain)
    return assigned_villain

def round(list):
    for player in list:
        villain = assign_villain(list[player])
        messagebox.showinfo(f"{list[player]} will play as {villain}")

def number_entry(player_num, villain_num):
    # Function to retrieve user input for number of players, save it in a global variable and display it.
    global number_of_players, number_of_villains, villains
    try:
        number_of_players = int(player_num)
        number_of_villains = int(villain_num)
    except ValueError:
        messagebox.showerror(title = "Not A Number", message = "Value entered is not a number")
    for v in range(0, number_of_villains):
        assigned_villain = random.choice(villains)
        villains.remove(assigned_villain)
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

def arrange_frame_3():
    i = 1
    Label(frame3, text = "First Round").grid(row = 0, column = 1, sticky = (W), columnspan = 3)
    for player in players:
        Label(frame3, text = "Player").grid(row = i, column = 1, sticky = (W))
        Label(frame3, text = player.name).grid(row = i, column = 2, sticky = (W))
        Label(frame3, text = player.villain).grid(row = i, column = 3, sticky = (W))
        i += 1
    next_round_button.grid(row = i + 1, column = 1, columnspan = 3, sticky = (W, E, N, S))

def next_round():
    pass

def update_player():
    global players, player_entry_entries
    name_valid = False
    for entry in player_entry_entries:
        if (len(entry.get()) > 9 or len(entry.get()) < 1):
            name_valid = True
    if name_valid:
        messagebox.showerror(title = "Input invalid", message = "Input entered was greater than 9 letters long or empty")
    else:
        for entry in player_entry_entries:  
            villain = assign_villain()
            name = entry.get()
            players.append(Player(name, villain, villains_played = villain))
    arrange_frame_3()
    for player in players:
        print(player.name, player.villain, player.score, player.villains)
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
submit_button_2 = Button(frame2, width = 7, text = "Submit", command = update_player)
back_button = Button(frame2, width = 7, text = "Back", command = go_back)

frame3 = ttk.Frame(root, padding = "3 3 12 12")
frame3.grid(column = 0, row = 0, sticky = (W, S, N, E))
frame3.rowconfigure(1, weight=1)
frame3.rowconfigure(2, weight=1)
frame3.columnconfigure(1, weight=1)
frame3.columnconfigure(2, weight=1)
next_round_button = Button(frame3, width = 7, text = "Next Round", command = next_round)

ttk.Label(frame2, text = "Enter the player names: ").grid(column = 1, row = 1, sticky = (W, S, N, E))

frame.tkraise()
root.update()
root.mainloop()