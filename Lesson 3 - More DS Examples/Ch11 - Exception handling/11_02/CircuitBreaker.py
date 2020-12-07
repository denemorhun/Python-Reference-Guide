""" Overloading a Circuit Breaker """


class CircuitBreaker:

    def __init__(self, max_amps):
        self.capacity = max_amps  # max capacity in amps
        self.load = 0             # present load in amps
        self.circuit_broken = False

    def connect(self, amps):
        if (self.load + amps) < 0:
                raise Exception ("Amperage cannot be negative")
        if self.circuit_broken is True:
            print("Cannot power device, check circuit.")
        else: 
            self.load += amps
            if self.load > self.capacity:
                self.circuit_broken = True
                print("You've exceed max amperage")

    def check_circuit(self):
        print("Circuit is broken" if self.circuit_broken else "All good.")

    def replace_fuse(self):
        print("Replacing fuse. Unplug and powerdown devices if possible.")
        self.circuit_broken = False
        self.load = 0

# create a 20A circuit breaker
cb = CircuitBreaker(20)
# cb.connect(30)
# cb.load