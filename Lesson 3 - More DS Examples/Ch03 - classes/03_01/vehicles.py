""" A Garage Full of Classy Vehicles """


class Vehicles:  # Base Vehicle class
    
    def __init__(self, color, manuf):
        self.color = color
        self.manuf = manuf
        self.gas = 4
        self.speed = 0
        self.helmet_on = False
        self.radio_on = False
        self.windows_down = False

    # drive vehicle as long as it has gas
    def drive(self):
        
        self.gas -= 1
        if self.gas > 0:
            print(f"The {self.color} {self.manuf} goes vroom!")
            self.speed = 10
        else:
            print("The engine sputters and dies...")
            self.speed = 0

    def inc_speed(self):
        self.speed += 5
        print(f"Speed: {self.speed}")
        if self.speed > 60:
            print("Max speed reached. Slow down")

    def dec_speed(self):
        self.speed -= 5
        
        if self.speed <= 0:
            print("Stopped.")
            self.speed = 0
        
        print(f"Speed: {self.speed}")


    # turn the radio on
    def radio(self):    
        print("Rockin' Tunes!")

    def fill_up(self):
        self.gas = 5
            
class Car(Vehicles): # Inherits from Vehicle class

    # open the window
    def window_down(self):
        print('Ahhh... fresh air!')
            
class Bike(Vehicles): # Inherits from Vehicle class
    
    # put on helmet
    def is_helmet_on(self):
        self.helmet_on = not self.helmet_on
        if self.helmet_on is True:
            print('Nice and safe!')
        else:
            print('Careful! Put on a helmet')
        return self.helmet_on

    # open the window
    def window_down(self):
        print('Bikes don\'t have windows')

    def drive(self):
        print('You mean ride a bike.')

class Bicycle(Bike):
    def start_pedalling(self):
        if super().is_helmet_on() is True:
            print('Off we go!')
            self.speed = 1
        else:
            print('Hey, put your helmet on, dude!')

    def inc_speed(self):
        self.speed += 1
        print(f"Speed: {self.speed}")
        if self.speed > 30:
            print("Max speed reached. Slow down")

    def fill_up(self):
        print("Bikes don't need gas")

class Motorbike(Bike):
    def ride(self):
        self.gas -= 1
        if self.gas > 0:
            print(f"The {self.color} {self.manuf} goes vroom!")
        else:
            print("The engine sputters and dies...")


# from vehicles import *
giant = Bicycle('yellow','giant')
harley = Motorbike('silver','harley')
bmw = Car('white','bmw')
pejo = Car('black','Peugeot')