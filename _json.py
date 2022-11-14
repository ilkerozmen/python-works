import json

# json str to dict

person_string = '{"name":"Ali","languages":["python","C#"]}'
person_dict = {"name":"Ali", "languages":["python","C#"]}

# result = json.loads(person_string)
# result = result["name"]
# result = result["languages"]


# with open("person.json") as f:
#     data=json.load(f)
#     print(data["name"])
#     print(data["languages"])

# dict to json str

# result = json.dumps(person_dict)
# print(result)
# print(type(result))


# with open("person.json","w") as f:
#     json.dump(person_dict,f)

person_dict = json.loads(person_string)
result = json.dumps(person_dict, indent=4, sort_keys=True)

print(person_dict)
print(result)