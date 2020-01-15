# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:

    def __init__(self, room, inv, hp):
        self.room = room
        self.inv = inv
        self.hp = hp 

    def __str__(self):
        return "You are in the {}. \nYou have in your bag: {}. \nYour HP is currently {}.".format(self.room, self.inv, self.hp)