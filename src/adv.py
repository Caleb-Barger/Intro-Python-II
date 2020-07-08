from room import Room
from player import Player
import sys

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Caleb", room['outside']) 

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
running = True
while running:
    print(player.current_room.name)
    print(player.current_room.desc)

    valid_inputs = ['n', 's', 'e', 'w', 'q']
    user_input= None
    while user_input not in valid_inputs:
        user_input= input("> ").lower()
        if user_input not in valid_inputs:
            print("not a valid move")
    
    if user_input== 'n':
        if not player.current_room.n_to == None:
            player.current_room = player.current_room.n_to
        else:
            print("Can't go that way try a diffrent direction")
            continue
    if user_input== 's':
        if not player.current_room.s_to == None:
            player.current_room = player.current_room.s_to
        else:
            print("Can't go that way try a diffrent direction")
            continue
    if user_input== 'e':
        if not player.current_room.e_to == None:
            player.current_room = player.current_room.e_to
        else:
            print("Can't go that way try a diffrent direction")
            continue
    if user_input== 'w':
        if not player.current_room.w_to == None:
            player.current_room = player.current_room.w_to
        else:
            print("Can't go that way try a diffrent direction")
            continue
    if user_input== 'q':
        do_quit = input("are you sure y/n: ").lower()
        if (do_quit == 'y'):
            sys.exit()
        continue


