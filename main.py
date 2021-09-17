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
rockets = [Rocket() for i in range(0,4)]
rocket_fleet.append(rockets)

for rockets in rocket_fleet:
    print(rockets[0],rockets[0].move_rocket(10,30))
    print(rockets[1],rockets[1].move_rocket(-30,40))
    print(rockets[2],rockets[2].move_rocket(10,90))
    print(rockets[3],rockets[3].move_rocket(5,16))


rocket2 = Rocket(80, 70)
print(f'\nDistance is {rocket2.get_distance(rocket1)}')
print(f'\nDistance between rocket0 and rocket2 in the fleet is {rockets[0].get_distance(rockets[2])}')

class Rocket2: 

  def __init__(self, color = 'white', passengers = 1): 
    self.color = color
    self.passengers = passengers

  def change(self, new_color, new_pass): 
    return self.new_color, self.new_pass


rocket0 = Rocket2('red', 3)
print()
print(rocket0.color, rocket0.passengers)

rocket_fleet0 = []
rocketz = [Rocket() for i in range (0,3)]
rocket_fleet.append(rockets)

for rocketz in rocket_fleet0: 
  print(rocketz[0].change('green', 9))
  print(rocketz[1].change('yellow', 100))
  print(rocketz[2].change('black', 40))


class rocket: 

  def land_rocket(self, x_val, y_val): 
    self.x_val = x_val
    self.y_val = y_val
    
    x_val -= x_val 
    y_val -= y_val 
    return x_val, y_val

ROCKET1 = rocket()
print()
rx = 30
ry = -30
print(rx,ry)
print(ROCKET1.land_rocket(rx,ry))

class Person: 

  def __init__(self, name, age, gender): 
    self.name = name
    self.age = age
    self.gender = gender

  def introduce_yourself(self): 
    return(f'Hello my name is {self.name}')

  def age_person(self): 
    new_age = self.age + 1
    return(f'In a year I will be {new_age} years old')

person1 = Person('Tenley', 16, 'Female')
print() 
print(person1.introduce_yourself())
print(person1.age_person())

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
