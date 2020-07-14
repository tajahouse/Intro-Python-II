# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, name, current_room):
    self.name = name
    self.current_room = current_room


  def move(self, direction):
    linked_room = self.current_room.other_rooms(direction)
    if linked_room is not None:
      self.current_room = linked_room
      print(f"You have entered the {linked_room.name}\n{linked_room.description}")
    else:
      print(f"That direction is not available. Try Again!!")


