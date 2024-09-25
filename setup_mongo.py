import pymongo

if __name__ == "__main__":
    mongo_client = pymongo.MongoClient()
    db = mongo_client['velouze']
