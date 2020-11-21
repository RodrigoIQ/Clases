class Field:
    def __init__(self):
        self.drunk_guy_location = {}

    def add_drunk_guy(self, drunkguy, location):
        self.drunk_guy_location[drunkguy] = location

    def move_drunk_guy(self, drunkguy):
        delta_x, delta_y = drunkguy.walkPatern()
        current_location = self.drunk_guy_location[drunkguy]
        new_location = current_location.movement(delta_x,delta_y)

        self.drunk_guy_location[drunkguy] = new_location

    def get_location(self, drunkguy):
        return self.drunk_guy_location[drunkguy]  
