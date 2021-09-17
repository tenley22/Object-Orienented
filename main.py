# Your Own Rocket 2 #
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
rockets = [Rocket() for i in range(0, 4)]
rocket_fleet.append(rockets)

for rockets in rocket_fleet:
    print(rockets[0], rockets[0].move_rocket(10, 30))
    print(rockets[1], rockets[1].move_rocket(-30, 40))
    print(rockets[2], rockets[2].move_rocket(10, 90))
    print(rockets[3], rockets[3].move_rocket(5, 16))

# Rocket Attributes #
rocket2 = Rocket(80, 70)
print(f'\nDistance is {rocket2.get_distance(rocket1)}')
print(f'\nDistance between rocket0 and rocket2 in the fleet is {rockets[0].get_distance(rockets[2])}')


class Rocket2: 

    def __init__(self, color='white', passengers=1, name='Default Rocket'):
        self.color = color
        self.passengers = passengers
        self.name = name

    def change(self, new_color, new_pass, new_name):
        self.color = new_color
        self.passengers = new_pass
        self.name = new_name
        return self.color, self.passengers, self.name


rocket0 = Rocket2('red', 3)
print()
print(rocket0.color, rocket0.passengers)

rocket_fleet0 = []
rocketz = [Rocket2() for i in range(0, 3)]
rocket_fleet0.append(rocketz)

for rocketz in rocket_fleet0: 
    print(rocketz[0].change('green', 15, 'Explorer'))
    print(rocketz[1].change('yellow', 100, 'Jupiter 19'))
    print(rocketz[2].change('black', 40, 'Dolly'))


class Rocket00:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def launch(self):
        return 'Lift Off!'

    def land_rocket(self):
        self.x -= self.x
        self.y -= self.y
        return self.x, self.y

    def get_distance(self, new_rocket):
        import math
        self.new_rocket = new_rocket
        x1 = new_rocket.x
        x2 = self.x
        y1 = new_rocket.y
        y2 = self.y
        distance = (x2 - x1) ^ 2 + (y2 - y1) ^ 2
        return math.sqrt(distance)

    def rocket_safety(self, other_rocket):
        self.other_rocket = other_rocket
        dist = self.get_distance(other_rocket)

        if dist <= 5:
            return 'Warning! These rockets are too close!'
        elif dist == 0:
            return 'Rockets have crashed!'
        else:
            return 'Rockets are at a safe distance'


ROCKET1 = Rocket00(30, -30)
print()
print(ROCKET1.launch())
print(30, -30)
print(ROCKET1.land_rocket())

ROCKET2 = Rocket00(40, 100)
print()
print(ROCKET2.rocket_safety(ROCKET1))

ROCKET3 = Rocket00(900, 900)
print(ROCKET3.rocket_safety(ROCKET2))


class Person: 

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def introduce_yourself(self):
        return f'Hello my name is {self.name}'

    def age_person(self):
        new_age = self.age + 1
        return f'In a year I will be {new_age} years old'

    def gender(self):
        return f'My gender is {self.sex}'


person1 = Person('Tenley', 16, 'Female')
print() 
print(person1.introduce_yourself())
print(person1.age_person())
print(person1.gender())


class Car:

    def __init__(self, color, seats, wheel_drive):
        self.color = color
        self.seats = seats
        self.wheel_drive = wheel_drive

    def describe_car(self):
        return f'This car is a {self.color} car with {self.seats} seats and {self.wheel_drive} wheel drive.'


car1 = Car('blue', 5, 4)
print()
print(car1.describe_car())

car2 = Car('grey', 8, 'all')
print(car2.describe_car())

car3 = Car('red', 2, 'rear')
print(car3.describe_car())
