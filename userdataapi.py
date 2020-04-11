#Use flask to make an api to get all user and user by id from the mysql dummy database ,authenticate request,create api endpoints for creating new user
#and update existing user details

from flask import Flask, request, jsonify, render_template, redirect, url_for, session
import mysql.connector  
import re

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/api/v1/resource/user/all', methods=['GET'])
def api_alluser():
    con=mysql.connector.connect(user='root', database='employees')
    cursor=con.cursor()
    cursor.execute('SELECT * FROM employees limit 3;')
    column=[column[0] for column in cursor.description]
    output = cursor.fetchall()
    alluser=[]
    for row in output:
        alluser.append(dict(zip(column,row)))
    return jsonify(alluser)

@app.route('/api/v1/resource/user', methods=['GET'])
def api_user_by_id():
    query_parameter=request.args
    for k,v in query_parameter.items():
        emp_no=k
        emp_value=v
    query = "SELECT * FROM employees WHERE " + emp_no + "=" + emp_value + ";"
    con=mysql.connector.connect(user='root', database='employees')
    cursor=con.cursor()
    cursor.execute(query)
    user=cursor.fetchall()
    return jsonify(user) 

'''    
@app.route('/api/v1/resource/adduser', methods=['POST'])
def api_adduser():
    con=mysql.connector.connect(user='root', database='employees')
    cursor=con.cursor()

    #cursor.execute('INSERT INTO employees (emp_no, birth_date,first_name,last_name,gender,hire_date) VALUES (11,1991,abhishek,tiwary,m,2020);')
    cursor.commit()
    addeduser="added user sucess"
    return jsonify(addeduser) 
'''    

if __name__ == '__main__': 
    app.run(debug=True)