class Player:
    
    def __init__(self, name, room_location):
        self.name = name
        self.room_location = room_location

    def move(self, direction):
        room_schemas = self.room_location.room_movement(direction)
        if room_schemas is not None:
            self.room_location = room_schemas
            print (f"\n{self.name} : You are now in the {room_schemas.name} area...N \n{room_schemas.description}")
        else:
            print("Room not available. Choose another direction!")
