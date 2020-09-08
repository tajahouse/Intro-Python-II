# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def room_movement(self, direction):
        if direction == 'N':
            return self.n_to
        elif direction == 'S':
            return self.s_to
        elif direction == 'E':
            return self.e_to
        elif direction == 'W':
            return self.w_to
        else:
            return None
