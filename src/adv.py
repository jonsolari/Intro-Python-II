from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons.", ["lamp"]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ["coin"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ["dagger"]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ["flask"]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", ["dust"]),
}


# Link rooms together

# room['outside'].n_to = room['foyer']
# room['foyer'].s_to = room['outside']
# room['foyer'].n_to = room['overlook']
# room['foyer'].e_to = room['narrow']
# room['overlook'].s_to = room['foyer']
# room['narrow'].w_to = room['foyer']
# room['narrow'].n_to = room['treasure']
# room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

choices = ["q", "i", "n", "e", "w", "s"]

player = Player('outside', ["Sword", "Amulet"], 40)

print()
print()
print("Welcome to Your Python Object-Oriented Adventure!")
print()
print("Type 'n' for North, 'w' for West, 's' for South, 'e' for East, 'i' for Inventory, or 'q' to Quit.")

while True:
    print()
    # print(player)
    print(room[player.room].desc)

    cmd = input("===> ")

    if cmd == "q":
        print("Thank you for playing!\n")
        break
    elif cmd == "i":
        print(player.inv)
    elif cmd == "n":
        print("\nGoing north...")
        if player.room == 'outside':
            player.room = 'foyer'
        elif player.room == 'foyer':
            player.room = 'overlook'
        elif player.room == 'narrow':
            player.room = 'treasure'
        else:
            print("You can't go that way.")
    elif cmd == "e":
        print("\nGoing east...")
        if player.room == 'foyer':
            player.room = 'narrow'
        else:
            print("You can't go that way.")
    elif cmd == "w":
        print("\nGoing west...")
        if player.room == 'narrow':
            player.room = 'foyer'
        else:
            print("You can't go that way.")
    elif cmd == "s":
        print("\nGoing south...")
        if player.room == 'foyer':
            player.room = 'outside'
        elif player.room == 'overlook':
            player.room = 'foyer'
        elif player.room == 'treasure':
            player.room = 'narrow'
        else:
            print("You can't go that way.")
    elif "look" in cmd:
        print("Items in room: ", room[player.room].items)
    elif "take" in cmd:
        input_query = set(cmd.split())
        new_stuff = input_query.intersection(room[player.room].items)
        for x in new_stuff:
            room[player.room].items.remove(x)
            player.inv.append(x)
            print("You have taken the", x)
        print("Items in room: ", room[player.room].items)
    elif "drop" in cmd:
        input_query = set(cmd.split())
        new_stuff = input_query.intersection(player.inv)
        for x in new_stuff:
            player.inv.remove(x)
            room[player.room].items.append(x)
            print("You have dropped the", x)
        print("Items in room: ", room[player.room].items)
    else:
        print("That is not a valid input.\n")


# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.