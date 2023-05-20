import random

def assign_villain(villain_list, player_assigned_villains, player):
    new_villain_list = []
    for value in villain_list:
        new_villain_list.append(value)
    assigned_villain = random.choice(new_villain_list)
    while assigned_villain.name in player_assigned_villains or assigned_villain.name in player.villains_played:
        new_villain_list.remove(assigned_villain)
        assigned_villain = random.choice(new_villain_list)
    player_assigned_villains.append(assigned_villain.name)
    return assigned_villain.name

def player_setup(player_list, player_assigned_villains, villain_list):
    for player in player_list:  
        p = [] 
        for value in player.villains_played:
            p.append(value)
        villain = assign_villain(villain_list, player_assigned_villains, player)
        #while villain in player.villains_played:
         #       villain = assign_villain(villain_list, player_assigned_villains)
        player.villain = villain
        p.append(villain)
        player.villains_played = p        
    player_assigned_villains.clear()
