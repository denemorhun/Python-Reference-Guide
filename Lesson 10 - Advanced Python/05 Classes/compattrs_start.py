# customize string representations of objects


class myColor():
    def __init__(self):
        self.red = 50
        self.green = 75
        self.blue = 100

    # TODO: use getattr to dynamically return a value
    def __getattr__(self, attr):
        if attr is "rgbcolor":
            return self.red, self.green, self.blue
        elif attr is 'hexcolor':
            return "#0:{self.red}{self.green}{self.blue}"
        else:
            raise AttributeError

    # TODO: use setattr to dynamically return a value
    def __setattr__(self, attr, val):
        if attr is 'rgbcolor':
            self.red = val[0]
            self.blue = val[1]
            self.green = val[2]
        else:
            super().__setattr__(attr, val)

    # TODO: use dir to list the available properties
    def __dir__(self):
        return ("red", "green", "blue", "rgbcolor")

def main():
    # create an instance of myColor
    cls1 = myColor()
    # TODO: print the value of a computed attribute
    print(cls1.rgbcolor)

    # TODO: set the value of a computed attribute

    print(cls1.rgbcolor)
    cls1.rgbcolor = (22, 44, 66)

    print(cls1.rgbcolor)
    
    
    # TODO: access a regular attribute
    cls1.blue = 200

    print('set new value to', cls1.blue) # 200

    # TODO: list the available attributes
    print(dir(cls1))


if __name__ == "__main__":
    main()
