class Director():
    """Director - class actually building the car"""
    def __init__(self, builder):
        self._builder = builder 
        
    def construct_car(self):
        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_engine()
        self._builder.add_tires()
        
    def get_car(self):
        # return whatever is stored in the builder object
        return self._builder.car
        
 
class Builder():
    """Abstract Builder"""
    def __init__(self):
        self.car = None 
        
    def create_new_car(self):
        self.car = Car()
        


class SkyLarkBuilder(Builder):
    """Concrete Builder --> provides parts and tools to work on the parts """
    
    def add_model(self):
        self.car.model = "Skylark"

    def add_tires(self):
        self.car.tires = "Regular tires"

    def add_engine(self):
        self.car.engine = "Turbo engine"

class FordFocusBuilder(Builder):
    """ Another concrete Builder"""

    def add_model(self):
        self.car.model = "Focus"

    def add_tires(self):
        self.car.tires = "Regular tires"

    def add_engine(self):
        self.car.engine = "Normal engine"

class Car():
    """Product"""
    def __init__(self):
        self.model = None
        self.tires = None
        self.engine = None
        
    def __str__(self):
        return '{} | {} | {}'.format(self.model, self.tires, self.engine)


# create a builder using the parts
builder = SkyLarkBuilder()
# director takes builder and uses it to build a car
car_temp = Director(builder)
car_temp.construct_car()
car = car_temp.get_car()

print(car)

fordbuild = FordFocusBuilder()

ford_temp = Director(fordbuild)
ford_temp.construct_car()
ford_car = ford_temp.get_car()
print(ford_car
)