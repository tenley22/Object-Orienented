class Rocket:

    def __init__(self, x_val = 0, y_val = 0):
        self.x_val = x_val
        self.y_val = y_val

    def move_rocket(self, x_loc, y_loc):
        self.y_loc = y_loc
        self.x_loc = x_loc
        self.y_val -= y_loc
        self.x_val += x_loc
        return self.x_val, self.y_val

    def get_distance(self, new_rocket):
        import math
        self.new_rocket = new_rocket
        x1 = new_rocket.x_val
        x2 = self.x_val
        y1 = new_rocket.y_val
        y2 = self.y_val
        distance = (x2-x1)^2+(y2-y1)^2
        return math.sqrt(distance)


rocket1 = Rocket()

for i in range(1):
    print(rocket1.move_rocket(10,20))
    print(rocket1.move_rocket(0, 30))
    print()

rocket_fleet = []
for i in range(10):
    rockets = Rocket(10, 50)
    rocket_fleet.append(rockets)

for rockets in rocket_fleet:
    print(rockets)
    print(rockets.move_rocket(10, 80))

rocket2 = Rocket(80, 70)
print(f'\nDistance is {rocket2.get_distance(rocket1)}')




