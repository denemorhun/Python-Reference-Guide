""" The Blueprints for Jeans """

class jeans:

    def __init__(self, waist, length, color):
        self.waist = waist
        self.length = length
        self.color = color
        self.wearing = False
    
    def put_on(self):
       # print('Putting on {}x{} {} jeans'.format(self.waist, self.length, self.color))
        self.wearing = True
        print(f'Putting on {self.waist}x{self.length} {self.color} jeans')

    def take_off(self):
        print(f'Taking off {self.waist}x{self.length} {self.color} jeans')
        self.wearing = False

def main():
    my_jean1 = jeans(31,31,"navy")
    my_jean1.put_on()
    print(my_jean1.wearing)
    my_jean1.take_off()
    print(my_jean1.wearing)

    my_jean2 = jeans(31,31,"black")
    my_jean1.put_on()
    my_jean2.take_off()

  #  print(type(my_jean1))
  #  print(type(my_jean2))

  #  print(dir(my_jean1))
  #  print(dir(my_jean2))

   

if __name__ == '__main__': main()

