from flask import Flask, redirect, render_template, url_for, request
from backend.models import order_page
import json

app = Flask(__name__)

@app.route('/')
def home_redirect():
    return redirect(url_for('home_render'))

@app.route('/home')
def home_render():
   return render_template('home.html')

@app.route('/order')
def order_render():
   return render_template('order_pesawat_page.html')

@app.route('/promo')
def promo_render():
   return render_template('promo_page.html')

@app.route('/result', methods=['GET','POST'])
def load_result():
   data = request.form
   json_file = open('static/json/flight_ticket.json')
   json_data = json.load(json_file)
   result = order_page.check_condition(data , json_data['flight_ticket'])
   return render_template("result_load.html",result=result)
   
if __name__ == '__main__':
   app.run("127.0.0.1", 5000, debug=True)