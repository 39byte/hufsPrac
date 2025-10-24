class Vehicle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

class Car(Vehicle):
    def __init__(self, name, speed,num_door = 4):
        super().__init__(name, speed)
        self.num_door = num_door

class Bus(Vehicle):
    def __init__(self, name, speed, num_pass):
        super().__init__(self, name, speed)
        self.num_pass = num_pass

c = Car("Avante", 180, num_door=4)
b = Bus("1150번", 120, 45)