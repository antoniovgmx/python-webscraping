import datetime
from pymongo import MongoClient
connectionString="mongodb+srv://admin:admin@cluster0.snt3m.mongodb.net/<dbname>?retryWrites=true&w=majority"
# localConnection=""
client = MongoClient(connectionString)
db=client.scraped
authors = db.authors

def queryDatabase(search_param):
    result = authors.find_one({ 'full_name' : search_param }, {'_id':False} )
    if(result is not None):
        return result
    else: 
        return None

def insertData(name, data):

    if(queryDatabase is not None):
        authors.replace_one({ 'full_name' : name }, {
        'name' : name,
        'date' : datetime.datetime.now(),
        'research_gate' : data['research_gate'],
        'google' : data['google']
        }) 
    else :
        authorid = authors.insert_one({ 'full_name' : name }, {
        'name' : name,
        'date' : datetime.datetime.now(),
        'research_gate' : data['research_gate'],
        'google' : data['google']
        }).inserted_id

    insertedData = queryDatabase(name)

    return insertedData
