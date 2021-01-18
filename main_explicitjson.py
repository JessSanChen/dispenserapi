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


class Ib(Resource):

    @app.route('/v1/resources/ib/all/', methods=['GET'])
    def get_all():
        data = []
        mycol = mydb['IB']

        cursor = mycol.find({"Usage_CC": {"$exists": True}})
        for doc in cursor:
            data.append(doc)

        return jsonify({"result": data})

    @app.route('/v1/resources/ib/query/', methods=['GET'])
    def get_request():
        data = []
        mycol = mydb['IB']

        param = request.get_json()

        Device_ID = param.get("Device_ID")
        StartTime = param.get("StartTime")
        EndTime = param.get("EndTime")

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
            try:
                json_doc = {
                    "_id": json.loads(json_util.dumps(doc["_id"])),
                    "Device_ID": doc["Device_ID"],
                    "Mac_Address": doc["Mac_Address"],
                    "UploadTime": doc["UploadTime"],
                    "TimeStamp": str(doc["TimeStamp"]),
                    "Hardware": doc["Hardware"],
                    "Status": doc["Status"],
                    "Heating": doc["Heating"],
                    "Cooling": doc["Cooling"],
                    "Refilling": doc["Refilling"],
                    "SavingPower": doc["SavingPower"],
                    "Sterilizing": doc["Sterilizing"],
                    "Hot_Valve": doc["Hot_Valve"],
                    "Warm_Valve": doc["Warm_Valve"],
                    "Cold_Valve": doc["Cold_Valve"],
                    "HotTemp": doc["HotTemp"],
                    "WarmTemp": doc["WarmTemp"],
                    "ColdTemp": doc["ColdTemp"],
                    "TDS": doc["TDS"],
                    "WaterLevel": doc["WaterLevel"],
                    "ErrorCode": doc["ErrorCode"],
                    "UserName": doc["UserName"],
                    "Consumption": doc["Consumption"],
                    "HotTemp_Insulation": doc["HotTemp_Insulation"],
                    "HotTemp_Insulation_High": doc["HotTemp_Insulation_High"],
                    "HotTemp_Insulation_Low": doc["HotTemp_Insulation_Low"],
                    "WarmTemp_Insulation": doc["WarmTemp_Insulation"],
                    "ColdTemp_Insulation": doc["ColdTemp_Insulation"],
                    "ColdTemp_Insulation_High": doc["ColdTemp_Insulation_High"],
                    "ColdTemp_Insulation_Low": doc["ColdTemp_Insulation_Low"],
                    "Filter_Usage": doc["Filter_Usage"],
                    "Filter_Hint": doc["Filter_Hint"],
                    "Usage_CC": doc["Usage_CC"],
                    "Usage_L": doc["Usage_L"],
                    "Usage_MT": doc["Usage_MT"],
                    "Meter": doc["Meter"],
                    "Current": doc["Current"]
                    }
            except KeyError:
                json_doc = {
                    "_id": json.loads(json_util.dumps(doc["_id"])),
                    "Device_ID": doc["Device_ID"],
                    "Mac_Address": doc["Mac_Address"],
                    "UploadTime": doc["UploadTime"],
                    "TimeStamp": str(doc["TimeStamp"]),
                    "Hardware": doc["Hardware"],
                    "Status": doc["Status"],
                    "Heating": doc["Heating"],
                    "Cooling": doc["Cooling"],
                    "Refilling": doc["Refilling"],
                    "SavingPower": doc["SavingPower"],
                    "Sterilizing": doc["Sterilizing"],
                    "Hot_Valve": doc["Hot_Valve"],
                    "Warm_Valve": doc["Warm_Valve"],
                    "Cold_Valve": doc["Cold_Valve"],
                    "HotTemp": doc["HotTemp"],
                    "WarmTemp": doc["WarmTemp"],
                    "ColdTemp": doc["ColdTemp"],
                    "TDS": doc["TDS"],
                    "WaterLevel": doc["WaterLevel"],
                    "ErrorCode": doc["ErrorCode"],
                    "UserName": doc["UserName"],
                    "Consumption": doc["Consumption"],
                    "HotTemp_Insulation": doc["HotTemp_Insulation"],
                    "HotTemp_Insulation_High": doc["HotTemp_Insulation_High"],
                    "HotTemp_Insulation_Low": doc["HotTemp_Insulation_Low"],
                    "WarmTemp_Insulation": doc["WarmTemp_Insulation"],
                    "ColdTemp_Insulation": doc["ColdTemp_Insulation"],
                    "ColdTemp_Insulation_High": doc["ColdTemp_Insulation_High"],
                    "ColdTemp_Insulation_Low": doc["ColdTemp_Insulation_Low"],
                    "Filter_Usage": doc["Filter_Usage"],
                    "Filter_Hint": doc["Filter_Hint"],
                    "Usage_CC": doc["Usage_CC"],
                    "Usage_L": doc["Usage_L"],
                    "Usage_MT": doc["Usage_MT"],
                    # "Meter": doc["Meter"],
                    # "Current": doc["Current"]
                }
            data.append(json_doc)

        return jsonify({'result': data})


@app.errorhandler(404)
def page_not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
