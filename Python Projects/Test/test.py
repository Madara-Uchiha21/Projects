import json

# Example JSON string
json_data = '''
{
    "name": "John",
    "age": 30,
    "city": "New York",
    "pets": [
        {"name": "Buddy", "species": "dog"},
        {"name": "Fluffy", "species": "cat"}
    ]
}
'''

# Deserialize JSON string to Python object
data = json.loads(json_data)

# Access specific data elements
name = data['name']
age = data['age']
city = data['city']
pet_names = [pet['name'] for pet in data['pets']]
pet_species = [pet['species'] for pet in data['pets']]

print("Name:", name)
print("Age:", age)
print("City:", city)
print("Pet Names:", pet_names)
print("Pet Species:", pet_species)