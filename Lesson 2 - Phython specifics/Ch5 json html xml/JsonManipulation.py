import json

# some JSON:
print("Input:\n")
json_data=  '{ "name":"Ege Orhun", "age":30, "city":"New York"}'

# parse x:
print("Example 1:\n")
parsed_json = json.loads(json_data)

# the result is a Python dictionary:
print(parsed_json)

#only get the age
print("The age is:", parsed_json["age"])

#convert the above back to json
print(json.dumps(parsed_json, indent=4, sort_keys=True))

print("Example 2:\n")
with open("/Users/dorhun/Desktop/Trainings/Python/Exercise Files/Misc/distros.json", "r") as f:
    distros_dict = json.load(f)

for distro in distros_dict:
    print(distro['Name'])