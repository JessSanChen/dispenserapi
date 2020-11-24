# Jessica Chen
# 11/19/2020
# BMW Lab


from bson import json_util
from flask import Flask, jsonify, request, make_response
from requests import get
from flask_restful import Api, Resource
from pymongo import MongoClient
import json

app = Flask(__name__)
api = Api(app)

PUBLIC_IP = get('https://api.ipify.org/').text

myclient = MongoClient('140.118.70.142:30708',
                       username='admin',
                       password='bmwee8097218',
                       authSource='admin',
                       authMechanism='SCRAM-SHA-1')
mydb = myclient.sc_dispenser


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Welcome!</h1><p>An API for water dispenser data.</p>'''


class Dispenser(Resource):

    @app.route('/v1/resources/query/', methods=['GET'])
    def get_request():
        param = request.get_json()

        Collection = param.get("Collection")
        Device_ID = param.get("Device_ID")
        StartTime = param.get("StartTime")
        EndTime = param.get("EndTime")

        data = []
        mycol = mydb[Collection]

        start = "2016-08-01 00:00:00"
        end = "2025-08-02 00:00:00"
        query = [{"Usage_CC": {"$exists": True}}]

        if Device_ID:
            query.append({"Device_ID": Device_ID})
        if StartTime:
            start = StartTime
            query.append({"UploadTime": {"$gte": start}})
        if EndTime:
            end = EndTime
            query.append({"UploadTime": {"$lt": end}})

        cursor = mycol.find({"$and": query})

        for doc in cursor:
            docdict = {}
            for line in doc:
                if "_id" in line:
                    doc[line] = json.loads(json_util.dumps(doc[line]))
                if "TimeStamp" in line:
                    doc[line] = str(doc[line])
                docdict[line] = doc[line]
            data.append(docdict)

        return jsonify({'result': data})


@app.errorhandler(404)
def page_not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
