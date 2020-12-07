class Borg:
    """The Borg design pattern"""

    _shared_state = {}

    def __init__(self):
        # a dictionary of attributes
        self.__dict__ = self._shared_state
    
class Singleton(Borg): 
    """The singleton class extends Borg, making shared state singleton a global variable"""

    def __init__(self, **kwargs):
        """update the attribute dictionary by inserting a kv pair"""
        Borg.__init__(self)
        self._shared_state.update(kwargs)
    
    def __str__(self):
        """toString method for attribute dict"""
        return str(self._shared_state.items())

x = Singleton(HTTP = "hyper text trans protocol")
print(x)

y = Singleton(XML = "HTML markup lang")
print(y)