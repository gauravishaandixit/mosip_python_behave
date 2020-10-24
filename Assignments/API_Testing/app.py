import flask
from flask import request, jsonify
import mysql.connector

app = flask.Flask(__name__)
conn = mysql.connector.connect(host = "localhost", user = "root", password = "ishaan", database = 'mosip')
cursor = conn.cursor()
cursor.execute('desc users')
columnNames = [row[0] for row in cursor.fetchall()]


@app.route('/')
def home():
    response = {'status_code': 406, 'data': {}}
    response['data']['email'] = 'Email already exists'
    return response


@app.route('/new_user', methods = ['POST'])
def addNewUser():
    data = request.get_json()
    cursor.execute('select * from users where email = %s', [data['email']])
    if len(cursor.fetchall()) > 0:
        response = {'status_code': 406, 'data': {}}
        response['data']['email'] = 'Email already exists'
        return response

    insertSQL = 'insert into users values (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
    insertValues = []
    for columnName in columnNames:
        insertValues.append(data[columnName])
    cursor.execute(insertSQL, insertValues)
    conn.commit()

    cursor.execute('select * from users where email = %s', [data['email']])
    rows = cursor.fetchall()
    print(rows)
    response = {'status_code': 200, 'data': dict(zip(columnNames, rows[0]))}
    return response



@app.route('/all_users', methods= ['GET'])
def allUsers():
    selectSQL = 'select * from users'
    cursor.execute(selectSQL)
    rows = cursor.fetchall()
    return jsonify(makeJSON(rows))


def makeJSON(rows):
    fullData = []
    for row in rows:
        data = dict(zip(columnNames, row))
        fullData.append(data)

    return fullData


app.run(debug=True)
