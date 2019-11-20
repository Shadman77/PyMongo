from pymongo import MongoClient

#Connect to database
client = MongoClient('mongodb://localhost:27017/')

#Get list of databases
print(client.list_database_names())

#Go to or create database
db = client['acme']

#Get list of collections of the database db
print(db.list_collection_names())

