from flask import Flask, jsonify, request, redirect, session, render_template
from flask_cors import CORS
from flask_session import Session
import modules.Data_functions as func
import secrets

app = Flask(__name__)


app.secret_key = 'ASDHFOT568As51@#'

@app.route("/")
def index():
    if session.get('is_verified')==True:
        return redirect('/protected-page')
    else:    
        return render_template('login_page.html')

@app.route('/', methods=['POST'])
def login():
    data = request.get_json()
    
    if func.verify(data['email'], data['password']):
        session['is_verified'] = True
        response_data = {"verified": "yes"}
    else:    
        response_data = {"verified": "no"}
        
    return jsonify(response_data)

@app.route('/protected-page', methods=['GET'])
def protected_page():
    if session.get('is_verified')==True:
        return render_template('index.html')
    else:
        return redirect('/')
    
@app.route('/protected-page', methods=['POST'])
def booking_data():
        user_data = request.get_json()

        name=user_data["Name"]
        email=user_data["Email"]
        people=user_data["Number of People"]
        room_type=user_data["Room Type"]
        phone=user_data["Phone Number"]

        room_no=func.booking(name,email,people,phone,room_type)
        return jsonify({"message":"Room Booked","Room No":room_no})

@app.route('/customer_info', methods=['GET'])
def customer_info_page():
    data=func.return_tabledata()
    if session.get('is_verified'):
        # You can add logic here to fetch customer info or display forms.
        return render_template('checkout.html',data=data)
    else:
        return redirect('/')







if __name__ == '__main__':
    app.static_folder = 'static'
    app.run(debug=True)

