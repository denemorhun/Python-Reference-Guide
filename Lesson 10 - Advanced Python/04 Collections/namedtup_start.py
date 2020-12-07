# Demonstrate the usage of namdtuple objects

import collections


def main():
    # TODO: create a Point namedtuple
    Point = collections.namedtuple("Point", 'x_coordinate y_coordinate')
   
    point_A = Point(x_coordinate=2, y_coordinate=3)
    point_B = Point(x_coordinate=10, y_coordinate=20)
    print(point_A)
    print(point_B)
    print(point_A + point_B)

    # TODO: use _replace to create a new instance
    pass
    print(point_A.x_coordinate)
    point_A = point_A._replace(x_coordinate=69)
    print("New coordinate is", point_A.x_coordinate)

if __name__ == "__main__":
    main()
