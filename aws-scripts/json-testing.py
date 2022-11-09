# kieran
# testing json configuration msg format
import json
x = {
    "field1" : 1,
    "field2": 2,
    "field3" : 3
}

x = json.dumps(x) # converts dict->json
print(x)