#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    capitals = {'United States': 'Washington, DC', 'France': 'Paris', 'Italy': 'Rome'}

    # Add Ankara, London, Moscow
    capitals['Turkey'] = 'Ankara'

    # join two dictionaries
    more_capitals = {'UK': 'London', 'Russia': 'Moscow', 'Germany':'Berlin'}
    capitals.update(more_capitals)

    # print("Print keys and values:")
    # for country, capital in capitals.items():
    #     print(f'The capital of {country} is {capital}')    

    # print("Use list comprehensions to generate lists and dictionaries:")
    # [ expression for item in list if conditional ]
    # print([capital for capital in capitals.values()]) 
    # print([country for country in capitals.keys()])

    # use list comprehension to switch keys and values
    print ({capital:country for country, capital in capitals.items()})

    # capital2country = {}
    # for country, capital in capitals.items():
    #     capital2country[capital] = country

    # print(capital2country)

    # for capital, country in capital2country.items():
    #     print(f'The capital of {country} is {capital}')

    # print("Print keys (countries) only using for loop:")
    # for country in capitals.keys():
    #     print(country)
    

    # print("Print values (capitals) only:")
    # for capital in capitals.values():
    #     print(capital)

    # print("Check if city is a capital:")
    # city = "Paris"
    # print(f'{city} is a capital city' if city in capitals.values() else f'{city} is a provincial city.')

    # print content of the dict

if __name__ == '__main__': main()
