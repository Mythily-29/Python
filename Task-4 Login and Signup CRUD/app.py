from flask import Flask,request,render_template,redirect,url_for
from models.config import dbconnect
from controllers.validations import email_exists,login_checkup
from controllers.sqlqueries import query_operations

app=Flask(__name__)
app.secret_key='delisha'

@app.route('/')
def validate_page():
    return render_template('frontpage.html')

@app.route('/signup')
def signup_page():
    return render_template('signup.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/checkdetails',methods=['POST'])
@email_exists
def check_signup():
    return redirect(url_for('login_page'))

@app.route('/main',methods=['POST'])
@login_checkup
def check_login():
    return render_template('login.html')

@app.route('/updatevalue',methods=['PUT'])
def admin_signup():
    data=request.get_json()
    if data['role'] and data['email']:
        query_operations(query='Update signedusers set role=%s where email=%s',values=(data.get('role'),data.get('email')),commit=True)

@app.route('/deletevalue',methods=['DELETE'])
def delete_user():
    data=request.get_json()
    if data.get('email'):
        query_operations(query='Delete from signedusers where email=%s',values=(data.get('email'),),commit=True)
if __name__=='__main__':
    app.run(debug=True)




