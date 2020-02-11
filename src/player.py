# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, current_room, item=1):
        self.current_room = current_room
        self.item = item
