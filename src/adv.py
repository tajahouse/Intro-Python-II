from room import Room
from player import Player

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

#a Since this will be a new player and will be the instance of the player class and room class, We will just need a function, not a class

def treasure_game():
    game_name = "Mansion Treasures"
    player = Player(game_name, room['outside'])
    print(f"You are now playing {game_name}.")


    player_input = input("Ready to play? Y for yes, N for no. \n").upper().strip()
    if player_input =="Y":
        name = input("What would you like to be called?").lower().strip()
        print(f"Nice to meet you {name}. You are currently {player.room_location.name}! \nHere is some info about where you are: {player.room_location.description}. \n Here you can move [N][S][E][W] or you can press [N] to quit...")
    elif player_input == "N":
        print("See you next time!")


treasure_game()
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
