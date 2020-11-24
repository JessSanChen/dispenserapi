from flask import Flask, jsonify, request, render_template
import pymssql
import datetime
import time
import json
from requests import get
from flask import make_response

app = Flask(__name__)

# if u can't "pip install pyodbc" -> $ sudo apt-get install unixodbc-dev
# then install again

# It will go to get its PUBLIC_IP, not need to adjust the code as change IP
# But port need to check it's used or not -> $ sudo netstat -tuap
PUBLIC_IP = get('https://api.ipify.org/').text


@app.route('/')
def home():
    return jsonify({'CPSi_API_Alive': 'True'})


##
# ============================
#        GET API
# ============================
# get /recent_data/cnc_five_axis
@app.route('/recent_data/cnc_five_axis')
def cnc_five_axis():
    conn = pymssql.connect(
        host='140.118.25.5',
        port='1433',
        user='sa',
        password='52075207',
        database='WEBACCESS_DEMO')

    cursor = conn.cursor()
    cursor.execute(
        'SELECT TOP 1 * FROM dbo.EventLog_1 ORDER BY LogDate DESC, LogTime DESC')  # dbo.EventLog_1 是Five-axis

    for row in cursor:
        print(row)

    row_tuple = tuple(row)
    # print(row_tuple)

    # print(row_tuple[0]) # ProjId
    # print(row_tuple[1]) # ProjNodeId
    # print(row_tuple[2]) # LogDate
    # print(row_tuple[3]) # LogTime
    # print(row_tuple[4]) # MilliSecond
    # print(row_tuple[5]) # Status
    # print(row_tuple[6]) # Voltage
    # print(row_tuple[7]) # Current
    # print(row_tuple[8]) # 不知道它是甚麼啊...一直都是-3000

    str_real_time = str(row_tuple[2])[0:11] + str(row_tuple[3])[11:]

    real_date_time = datetime.datetime.strptime(str_real_time, '%Y-%m-%d %H:%M:%S')
    # print(real_date_time)
    # print(type(real_date_time))

    Send_data = {'ProjId': row_tuple[0], 'ProjNodeId': row_tuple[1], 'DateTime': real_date_time,
                 'MilliSecond': row_tuple[4], 'Status': row_tuple[5], 'Voltage': row_tuple[6], 'Current': row_tuple[7],
                 'Data4': row_tuple[8]}
    print(Send_data)
    # print(type(Send_data))

    return jsonify(Send_data)


# get /recent_data/cnc_lathe
@app.route('/recent_data/cnc_lathe')
def get_cnc_lathe():
    conn = pymssql.connect(
        host='140.118.25.5',
        port='1433',
        user='sa',
        password='52075207',
        database='WEBACCESS_DEMO')

    cursor = conn.cursor()
    cursor.execute('SELECT TOP 1 * FROM dbo.EventLog_2 ORDER BY LogDate DESC, LogTime DESC')  # dbo.EventLog_2 是Lathe

    for row in cursor:
        print(row)

    row_tuple = tuple(row)
    # print(row_tuple)

    # print(row_tuple[0]) # ProjId
    # print(row_tuple[1]) # ProjNodeId
    # print(row_tuple[2]) # LogDate
    # print(row_tuple[3]) # LogTime
    # print(row_tuple[4]) # MilliSecond
    # print(row_tuple[5]) # Status
    # print(row_tuple[6]) # Voltage
    # print(row_tuple[7]) # Current
    # print(row_tuple[8]) # 不知道它是甚麼啊...一直都是-3000

    str_real_time = str(row_tuple[2])[0:11] + str(row_tuple[3])[11:]

    real_date_time = datetime.datetime.strptime(str_real_time, '%Y-%m-%d %H:%M:%S')
    # print(real_date_time)
    # print(type(real_date_time))

    Send_data = {'ProjId': row_tuple[0], 'ProjNodeId': row_tuple[1], 'DateTime': real_date_time,
                 'MilliSecond': row_tuple[4], 'Status': row_tuple[5], 'Voltage': row_tuple[6], 'Current': row_tuple[7],
                 'Data4': row_tuple[8]}
    print(Send_data)
    # print(type(Send_data))

    return jsonify(Send_data)


# get /recent_data/cnc_three_axis
@app.route('/recent_data/cnc_three_axis')
def get_cnc_three_axis():
    conn = pymssql.connect(
        host='140.118.25.5',
        port='1433',
        user='sa',
        password='52075207',
        database='WEBACCESS_DEMO')

    cursor = conn.cursor()
    cursor.execute(
        'SELECT TOP 1 * FROM dbo.EventLog_3 ORDER BY LogDate DESC, LogTime DESC')  # dbo.EventLog_3 是Three-axis

    for row in cursor:
        print(row)

    row_tuple = tuple(row)
    # print(row_tuple)

    # print(row_tuple[0]) # ProjId
    # print(row_tuple[1]) # ProjNodeId
    # print(row_tuple[2]) # LogDate
    # print(row_tuple[3]) # LogTime
    # print(row_tuple[4]) # MilliSecond
    # print(row_tuple[5]) # Status
    # print(row_tuple[6]) # Voltage
    # print(row_tuple[7]) # Current
    # print(row_tuple[8]) # 不知道它是甚麼啊...一直都是-3000

    str_real_time = str(row_tuple[2])[0:11] + str(row_tuple[3])[11:]

    real_date_time = datetime.datetime.strptime(str_real_time, '%Y-%m-%d %H:%M:%S')
    # print(real_date_time)
    # print(type(real_date_time))

    Send_data = {'ProjId': row_tuple[0], 'ProjNodeId': row_tuple[1], 'DateTime': real_date_time,
                 'MilliSecond': row_tuple[4], 'Status': row_tuple[5], 'Voltage': row_tuple[6], 'Current': row_tuple[7],
                 'Data4': row_tuple[8]}
    print(Send_data)
    # print(type(Send_data))

    return jsonify(Send_data)


# get /recent_data/aircondition
@app.route('/recent_data/aircondition')
def get_aircondition():
    conn = pymssql.connect(
        host='140.118.25.5',
        port='1433',
        user='sa',
        password='52075207',
        database='WEBACCESS_DEMO')

    cursor = conn.cursor()
    cursor.execute('SELECT TOP 1 * FROM dbo.EventLog_7 ORDER BY LogDate DESC, LogTime DESC')  # dbo.EventLog_7 是 8台冷氣機

    for row in cursor:
        print(row)

    row_tuple = tuple(row)

    str_real_time = str(row_tuple[2])[0:11] + str(row_tuple[3])[11:]

    real_date_time = datetime.datetime.strptime(str_real_time, '%Y-%m-%d %H:%M:%S')
    # print(real_date_time)
    # print(type(real_date_time))

    Send_data = {'ProjId': row_tuple[0], 'ProjNodeId': row_tuple[1], 'DateTime': real_date_time,
                 'MilliSecond': row_tuple[4], 'A1_Voltage': row_tuple[5], 'A1_Current': row_tuple[6],
                 'A2_Voltage': row_tuple[7], 'A2_Current': row_tuple[8], 'A3_Voltage': row_tuple[9],
                 'A3_Current': row_tuple[10], 'A4_Voltage': row_tuple[11], 'A4_Current': row_tuple[12],
                 'A5_Voltage': row_tuple[13], 'A5_Current': row_tuple[14], 'A6_Voltage': row_tuple[15],
                 'A6_Current': row_tuple[16], 'A7_Voltage': row_tuple[17], 'A7_Current': row_tuple[18],
                 'A8_Voltage': row_tuple[19], 'A8_Current': row_tuple[20]}
    # print(Send_data)

    return jsonify(Send_data)


# get /recent_data/agv
@app.route('/recent_data/agv')
def get_agv():
    conn = pymssql.connect(
        host='140.118.25.13',
        port='1433',
        user='john',
        password='john',
        database='factory')

    cursor = conn.cursor()
    cursor.execute('SELECT TOP 1 * FROM factory.dbo.Agv_status ORDER BY AGV_id DESC')

    for row in cursor:
        print(row)
        row_tuple = tuple(row)
    Send_data = {'AGV_id': row_tuple[0], 'Map_Location': row_tuple[1], 'Car_num': row_tuple[2],
                 'Car_name': row_tuple[3], 'CarKind': row_tuple[4], 'AGV_ip': row_tuple[5], 'Port': row_tuple[6],
                 'AGVState': row_tuple[7], 'Heading': row_tuple[8], 'AGVPosiTion_X': row_tuple[9],
                 'AGVPosiTion_Y': row_tuple[10], 'Real_X': row_tuple[11], 'Real_Y': row_tuple[12],
                 'CAD_X': row_tuple[13], 'CAD_Y': row_tuple[14], 'AGV_NowNode': row_tuple[15],
                 'Next_Node': row_tuple[16], 'Using_Zone': row_tuple[17], 'Nature': row_tuple[18],
                 'Power': row_tuple[19], 'Electricity': row_tuple[20], 'RemainingWeight': row_tuple[21],
                 'Temperture': row_tuple[22], 'RemainingBox': row_tuple[23], 'UptimeRrate': row_tuple[24],
                 'DailyWorkTime': row_tuple[25], 'DailyOperationTime': row_tuple[26], 'WaiTing_time': row_tuple[27],
                 'DailyWaiTingTime': row_tuple[28], 'RecordDateTime': row_tuple[29]}

    return jsonify(Send_data)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found QAQ'}), 404)


app.run(host=PUBLIC_IP, port=1106)