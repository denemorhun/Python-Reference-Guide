#
# Example file for working with classes
#


class myClass():
    def method1(self):
        print("myClass method1")

    def method2(self, someString):
        print("myClass method2 " + someString + " " )


# inherit from parents class

class babyClass(myClass):
    def method1(self):
        print("baby method1")

    def method2(self, someString):
        print("baby method2 ")



def main():
    c = myClass()
    # call the methods of the class
    c.method1()
    c.method2("HERA is sleeping")

    c2 = babyClass()
    c2.method1()
    c2.method2("Hera is awake")


if __name__ == "__main__":
  main()
