import json

json_data = '{"name": "Sara", "marks": 90}'
data = json.loads(json_data)

print(data["name"])