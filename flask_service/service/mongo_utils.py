
import pymongo

database = "mydatabase"

def insert(collection, record):

    print "writing record: {} to {}".format(record, collection)

    # because mongo-service is specified in docker-compose
    # we can use it to specify the service
    myclient = pymongo.MongoClient("mongodb://mongo-service:27017/")

    mydb = myclient[database]
    mycol = mydb[collection]

    mycol.insert(record)
    
    print "Done"

