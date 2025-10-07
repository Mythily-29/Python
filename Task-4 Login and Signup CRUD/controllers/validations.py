from flask import request,jsonify,redirect,url_for,flash,render_template
from functools import wraps
from controllers.sqlqueries import query_operations
from datetime import datetime 

now = datetime.now()
formatted = now.strftime("%Y-%m-%d %H:%M:%S")

def email_exists(f):
    @wraps(f)
    def checking_details(*args,**kwargs):
        email=request.form.get('email')
        name=request.form.get('name')
        password=request.form.get('password')
        role=request.form.get('role')
        data=query_operations(query='SELECT * from signedusers where email=%s',values=(email,),fetch=True)
        
        if data:
            flash('Email exists','error')
            return redirect(url_for('signup_page'))
        query_operations(query='INSERT into signedusers(role,username,email,password,created_at) values(%s,%s,%s,%s,%s)',values=(int(role),name,email,password,formatted),commit=True)
        return f(*args,**kwargs)
    return checking_details


def login_checkup(f):
    @wraps(f)

    def checking_login_details(*args,**kwargs):
        email=request.form.get('email')
        password=request.form.get('password')

        data=query_operations(query='Select role,email from signedusers where email=%s and password=%s',values=(email,password),fetch=True)

        if data:
            user=query_operations(query='Select * from signedusers',fetch=True)
            if data[0][0]==0:
                return render_template('usersdisplay.html',users=user)
            else:
                return render_template('admindisplay.html',users=user)
            # return {'data':request.form}
        return f(*args,**kwargs)
    return checking_login_details





