import copy

class Prototype:
    
    def __init__(self):
        self._objects = {}
        
    def register_object(self, name, obj):
        """Register an object"""
        self._objects[name] = obj
          
    def unregister_object(self, name):
        """Unregister an object"""
        del self._objects[name]
        
    def clone(self, name, **attr):
        """Clone a registered object and update its attributes"""
        obj = copy.deepcopy(self._objects.get(name))
        # update the cloned object based on the attributes
        obj.__dict__.update(attr)
        return obj

class Car:
    def __init__(self):
        self.name = "ford"
        self.color = "Red"
        self.options = "Ex"
        
    def __str__(self):
        return '{} | {} | {}'.format(self.name, self.color, self.options)
        
# first instantiate the car class

c = Car()
prop = Prototype()
prop.register_object("ford", c)

c1 = prop.clone("ford")
print(c1)

prop.unregister_object(c1)
print(c1)
