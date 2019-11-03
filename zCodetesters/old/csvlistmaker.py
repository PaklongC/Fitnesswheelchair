import csv, json
with open('test1.csv', 'r') as f:
    reader = csv.reader(f)
    your_list = list(reader)
print(your_list)
y = json.dumps(your_list)
print(str(y))
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))
