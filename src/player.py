class Player:
    
    def __init__(self, name, room_location):
        self.name = name
        self.room_location = room_location

    def move(self, direction):
        room_schemas = self.room_location.all_rooms(direction)
        if room_schemas is not None and len(room_schemas.items) < 0:
            self.room_location = room_schemas
            print (f"\n{self.name} : You are now in the {room_schemas.name} area \n Room Info: {room_schemas.description}")
        else:
            print("Room not available. Choose another direction!")
