#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

animals = ( 'bear', 'bunny', 'dog', 'cat', 'velociraptor' )

for pet in animals:
    if pet == 'bear': continue
    if pet == 'velociraptor': break
    print(pet)
else:
    print("that's all folks")

