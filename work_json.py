import json
collage = {
    "collage": "Engineering Collage",
    "objectives": "Mastering CS",
    "department": {
        "dep1": "Electrical",
        "dept2": "CS"
    },
    "years": [
        "year 1",
        "year 2",
        "year 3",
        "year 4"
    ],
    "numbers":[1,2,3,4],
    "ID": [10,20,30,40]
}

# Writing and reading from JSON
json.dump(collage, open("collage.json", "w"))
new_collage = json.load(open("collage.json", "r"))
print(new_collage)
