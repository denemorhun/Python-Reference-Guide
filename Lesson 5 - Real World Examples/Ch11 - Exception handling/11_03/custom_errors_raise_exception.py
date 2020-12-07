""" Handling Household Problems """

from random import randint

class ElectricalError(Exception):
    
    def __init__(self, device, problem):
        self.device = device
        self.problem = problem
        
    def __str__(self):
        return "The {} is {}!".format(self.device, self.problem)


class PlumbingError(Exception):
    
    def __init__(self, device, problem):
        self.device = device
        self.problem = problem
        
    def __str__(self):
        return "The {} is {}!".format(self.device, self.problem)

class GhostError(Exception):
    
    def __init__(self, device, problem):
        self.device = device
        self.problem = problem
        
    def __str__(self):
        return "The {} is {}!".format(self.device, self.problem)

class InternetError(Exception):
    def __init__(self, device, problem):
        self.device = device
        self.problem = problem

    def __str__(self):
        return "The {} is {}!".format(self.device, self.problem)


def cause_error(error_type):

    if error_type == 'electrical':
        raise ElectricalError('circuit breaker', 'overloaded')
    
    elif error_type == 'plumbing':
        raise PlumbingError('dishwasher', 'spraying water')

    elif error_type == 'internet':
        raise InternetError('router','flashing orange lights')

    elif error_type == 'ghost':
        raise GhostError('Ghost', 'booo')

    else:
        raise Exception("There is something else going on")

def main():
   # cause_error('electrical')

    cases = {1:"electrical", 2:"plumbing", 3:"internet", 4:"tree", 5:"ghost"}
    
    try:
        cause_error(cases[randint(1,5)])

    except ElectricalError as e:
        print(e)
        print('Call electrician')
    
    except PlumbingError as e:
        print(e)
        print('Call the plumber')

    except GhostError as e:
        print(e)
        print('Call the Ghostbusters')

    except:
        print('Call the landlord')

if __name__=="__main__":
    main()