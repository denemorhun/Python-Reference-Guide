#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    students = [('denem', 'B', 38),('ege','A',3),('seda','C',30)]

    # should sort by names
    print(sorted(students, key=lambda student:student[0]))
    
    # should sort by letter
    print(sorted(students, key=lambda student:student[1]))

    # should sort by age
    print(sorted(students, key=lambda student:student[2]))


if __name__ == '__main__': main()
