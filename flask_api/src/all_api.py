'''
Created on Nov 16, 2020

@author: apratim
'''
import flask
from flask import request, jsonify
import read_data

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Get the raw_data
raw_data = read_data.load_incident_data()


@app.route('/', methods=['GET'])
def home():
    return '''<h1>APIs to get the incident data</h1>
    <p>Based on the organisation requirement, every day thousand of Incidents are registered on the ticketing tools, like Service Now, from which they are processed, assigned and closed.</p>
    <p>Based on use-cases we came up with analysis requirements in three specific areas of concern -</p>
    <ul>
        <li>Predicting Priority of Tickets: so that we can take preventive measures or fix the problem before it surfaces.</li>
        <li>Predict RFC (Request for change) and possible failure/misconfiguration of assets.</li>
        <li>Forecast the incident volume iso that they can be better prepared with resources and technology planning.</li>
    </ul>'''


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/get-raw-data', methods=['GET'])
def api_all():
    query_parameters = request.args
    limit = query_parameters.get('limit')
    if(limit):
        limited_data = raw_data[:int(limit)]
        return limited_data.to_json(orient='records'),200,{'Content-Type': 'application/json'}
    else:
        return internal_server_error("Limit must be defined")

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

@app.errorhandler(500)
def internal_server_error(e):
    return "<h1>500</h1><p>" + e + "</p>", 500
