from flask import Flask, request, jsonify
import mysql.connector as sql
import random
db=sql.connect(
    host="localhost",
    user="root",
    password="",
    database="empdirect")
cursor=db.cursor()
app = Flask(__name__)
users = {}


@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    email=data.get("email")
    

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email=data.get("email")
    password = data.get('password')
    print(email,password)
    query="select * from user where email=%s and password=%s"
    cursor.execute(query,(email,password))
    result=cursor.fetchone()
    print(result)
    if result:
        users[result[0]]={'username':result[1], 'loggedin':True}
        return jsonify({'status':'Logged In','userid':result[0]})
    else:
        return jsonify({'status':'Failed to LogIn'})


if __name__ == '__main__':
    app.run(debug=True)
