
import pymongo

database = "mydatabase"

def insert(collection, record):

    print "writing record: {} to {}".format(record, collection)

    # myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    myclient = pymongo.MongoClient("mongodb://192.168.0.4:27017/")

    mydb = myclient[database]
    mycol = mydb[collection]

    mycol.insert(record)
    
    print "Done"

