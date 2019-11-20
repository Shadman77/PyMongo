from pymongo import MongoClient

# Connect to database
# client = MongoClient('mongodb://localhost:27017/')#local
client = MongoClient(
    'mongodb+srv://shadman_saif:01818285563@data-vcbev.mongodb.net/test?retryWrites=true&w=majority')  # atlas

# Get list of databases
print('List of databases')
print(client.list_database_names())

# Go to or create database
db = client['test']

# Get list of collections of the database db
print('List of collection')
print(db.list_collection_names())

# get all entries
collection = db['posts']
print(collection.find()[0])
for doc in collection.find():
    print(doc)

# Inserting data
print()
print('Inserting Data:')
pyDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "colors": ['red', 'green', 'blue'],
    'address': {
        "state": 'New York',
        "country": 'USA',
    }
}


# print(pyDict)
# result = collection.insert_one(pyDict)#inserting
# print(result.inserted_id)

# Updating Data
print()
print('Updating Data:')
pyDict['model'] = 'Focus'
pyDict['year'] = 2018
print(pyDict)
result = collection.replace_one({'title': 'Document 1'}, pyDict, True)
print(result.matched_count)
print(result.modified_count)
