from flask import Flask, request
from researchGate import findResearchGate
from googleAcademic import findGoogle

app = Flask(__name__)

@app.route('/<string:name>')
def query_by_name(name):

    return {
        "research_gate" : findResearchGate(name),
        "google" : findGoogle(name)
    }


if __name__ == "__main__":
    app.run(debug=True)