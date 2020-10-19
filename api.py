from flask import Flask, request, jsonify
from researchGate import findResearchGate
from googleAcademic import findGoogle
from database import queryDatabase, insertData, insertTest, replaceTest
from bson import json_util

app = Flask(__name__)

# Consulta la base de datos, de no tener datos se hace el scrape
@app.route('/<string:name>')
def query_by_name(name):

    queryResult = queryDatabase(name)
    if(queryResult != None):
        return queryResult
    else:
        scrapeResults = {
            'research_gate' : findResearchGate(name),
            'google' : findGoogle(name)
        }

        insertedData = insertData(name, scrapeResults)
        
        return insertedData

# Consulta únicamente la base de datos
@app.route('/db/<string:name>')
def query(name):
    results = queryDatabase(name)
    if(results != None):
        print (results)
        return results
    else:
        return { 'error' : 'Sin resultados' }

# Realiza únicamente el scrape, sin guardar los resultados 
@app.route('/scrape/<string:name>')
def scrape(name):

    return {
        "research_gate" : findResearchGate(name),
        "google" : findGoogle(name)
    }

# Testing
@app.route('/test/insert/<string:name>')
def testinsertendpoint(name):

    try:
        insertTest(name)
        return "Success"
    except:
        return "Fail"



# Testing
@app.route('/test/replace/<string:name>')
def testreplaceendpoint(name):

    try:
        replaceTest(name)
        return "Success"
    except:
        return "Fail"




if __name__ == "__main__":
    app.run(debug=True)