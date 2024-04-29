from pymongo import MongoClient, errors
from bson.json_util import dumps
import os
import json

MONGOPASS = os.getenv('MONGOPASS')
uri = "mongodb+srv://mvu2ab:sdugQHXvKeQ9wizT@cluster0.fjhtrum.mongodb.net/"
client = MongoClient(uri, username= 'mvu2ab', password='Chestnutstreet25!', connectTimeoutMS=200, retryWrites=True)
db = client.mvu2ab
collection = db.collection1

def import_json_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            try:
                file_path = os.path.join(directory, filename)
            except Exception as e:
                print(filename, e)
            with open(file_path) as file:
                try:
                    data = json.load(file)
                except Exception as e:
                    print(filename, e)
                if isinstance(data, list):
                    collection.insert_many(data)
                else:
                    collection.insert_one(data)

def main():
    directory = "data"
    import_json_files(directory)

if __name__ == "__main__":
    main()

path = 'data'
for (root, dirs, file) in os.walk(path):
    for f in file:
        print(f)