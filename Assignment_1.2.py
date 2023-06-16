import json

indian_states = """{
    "Maharashtra": "pune",
    "Karnataka": "Bengaluru",
    "Tamil Nadu": "madhurai",
    "Uttar Pradesh": "Lucknow",
    "Gujarat": "amhemdhad",
    "Rajasthan": "jodhapur",
    "West Bengal": "Kolkata"
}"""

# # convert json object to dict
dict_obj = json.loads(indian_states)
print(dict_obj)
print(type(dict_obj))

# # convert dict object to json
json_obj = json.dumps(dict_obj)
print(json_obj)
print(type(json_obj))





