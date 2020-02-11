from src.item import Item
from src.room import Room
from src.player import Player
import textwrap


# Declares all the Items

items = {
    'sword': Item('sword'),
    'shield': Item('shield'),
    'treasure': Item('treasure'),
    'potion': Item('potion'),
}


# Declare all the rooms

room = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons", [items['sword'], items['shield']]),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [items['shield']]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [items['potion']]),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [items['potion']]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [items['treasure']]),
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
player = Player(room['outside'])

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
    current_room = player.current_room
    room_name = player.current_room.name
    room_items = player.current_room.items
    empty_room = True

    error_msg = 'This is a Dead End'

    print(f"You are in: \n{room_name}")
    print(textwrap.wrap(player.current_room.desc))

    if room_items is not []:
        print("\nThis room contains:")
        for i in room_items:
            print(i)
        empty_room = False

    value = input(f"\nEnter a Command:\nn: North \ns: South \ne: East \nw: West\np: Pickup Item\nd: Drop Item\ni: "
                  f"View Inventory\n")
    value = value.upper()
    # todo Replace elif Chain with Switch-Case statement
    if value == 'N':
        if player.current_room.n_to is not None:
            player.current_room = player.current_room.n_to
        else:
            print(error_msg)
    elif value == 'S':
        if player.current_room.s_to is not None:
            player.current_room = player.current_room.s_to
        else:
            print(error_msg)
    elif value == 'E':
        if player.current_room.e_to is not None:
            player.current_room = player.current_room.e_to
        else:
            print(error_msg)
    elif value == 'W':
        if player.current_room.w_to is not None:
            player.current_room = player.current_room.w_to
        else:
            print(error_msg)
    elif value == 'P':
        if empty_room:
            print("The Room is empty")
        else:
            cmd = input("Which item would you like to pickup?").lower()
            for i in room_items:
                if i.name == cmd:
                    player.add_item(i)
                    current_room.remove_item(i)
                    print(f"Picked up {cmd}")
                    break

    elif value == 'I':
        print('\nInventory:')
        for i in player.items:
            print(i)
    elif value == 'D':
        print("\n Which item would you like to drop?")
        for i in player.items:
            print(i)
        choice = input("").lower()
        for i in player.items:
            if i.name == choice:
                player.remove_item(i)
                current_room.add_item(i)
                print(f"Dropped {choice}")
                break

    elif value == 'Q':
        running = False
        break
