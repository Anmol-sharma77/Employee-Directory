from flask import Flask, request, jsonify,make_response
from flask_cors import CORS
import random
app = Flask(__name__)
CORS(app)
import mysql.connector as sql
db=sql.connect(
    host="localhost",
    user="root",
    password="",
    database="empdirect")
cursor=db.cursor()


@app.route('/signup', methods=['POST'])
def signup():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        email=data.get("email")
        query="select * from user where email=%s"
        cursor.execute(query, (email,))
        result=cursor.fetchone()
        if result:
            return make_response('', 400)
        id=random.randrange(340,2000)
        query = """INSERT INTO user (userid,name, password, email,role) VALUES(%s,%s,%s,%s,%s)"""
        cursor.execute(query,(id,username,password,email,"user"))
        db.commit()
        return make_response('', 200)

    except Exception as e:
        print(e)
        return make_response('', 400)


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email=data.get("mail")
    password = data.get('password')
    print(email,password)
    query="select * from user where email=%s and password=%s"
    cursor.execute(query,(email,password))
    result=cursor.fetchone()
    print(result)
    if result:   
        return make_response('', 200)
    else:
        return make_response('', 400)


if __name__ == '__main__':
    app.run(debug=True)
