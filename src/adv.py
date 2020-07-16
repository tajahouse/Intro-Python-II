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


directions={"n", "s", "e", "w"}
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
def text_game():
    name = "Endless Treasure Hunt"
    player = Player(name, room['outside'])
    print("\nWelcome to Endless Treasure Hunt. Would you like to play?")

    user_input = input("\nEnter [P] to Start or [Q] to Quit: ").lower().strip()

    if user_input == "p":
        name = input("\nWhat shall I call you Adventurer?:").upper().strip()
        if name != '':
            player.name = name
        print(f"\nTime to start your journey Adventurer {player.name}:\n\nAt present you are at the {player.current_room.name}\nInfo: {player.current_room.description}\n\nTo start your journey choose a direction: [N]/[S]/[E]/[W] or [Q] to Quit\n\n")
    elif user_input != "p":
        print("\nThanks for Playing! GoodBye UnKnown Adventurer!")
# Write a loop that:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
    while user_input == "p":
        choice = input("Which direction will you choose?:")
        if choice.lower().strip() in directions:
            player.move(choice)
        elif choice == 'q':
            print(f"\nThanks for Playing! GoodBye Adventurer {player.name}!")
            sys.exit()
# If the user enters "q", quit the game.



text_game()