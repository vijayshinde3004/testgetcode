import pymongo
client = pymongo.MongoClient("mongodb+srv://vijay:vijay123@mongodb.cu4pzqh.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)


d={
    "name":"vijay",
    "emailid":"vijay123",
    "surname":"shinde"
}
db1=client["mongotest"]
coll=db1["test"]
coll.insert_one(d)