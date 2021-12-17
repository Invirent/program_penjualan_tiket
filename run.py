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
   if request.method == "POST":
      data = request.form
      json_file = open('static/json/flight_ticket.json')
      json_data = json.load(json_file)
      result = order_page.check_condition(data , json_data['flight_ticket'])
      return render_template("result_load.html",result=result)
   else:
      return render_template("order_pesawat_page.html")

@app.route('/result/<flight>')
def flight_order(flight):
   flight = flight.replace("'",'"')
   flight = flight.replace("None","null")
   flight = flight.replace("economy","Economy")
   flight = flight.replace("business","Business")
   flight = flight.replace("first_class","First Class")
   flight = json.loads(flight)
   return render_template("flight_result.html",flight = flight)

@app.route('/result/payment', methods=['GET','POST'])
def redirect_payment():
   if request.method == "POST":
      data = request.form
      flight_str = data['flight']
      flight_str = flight_str.replace("'",'"')
      flight_str = flight_str.replace("None","null")
      flight_order = json.loads(flight_str)
      number_of_ticket = data['number_of_ticket']
      flight_order['number_of_ticket'] = number_of_ticket
      flight_order['total_price'] = flight_order['price_per_ticket'] * number_of_ticket
      return render_template("render_payment.html", flight_order=flight_order)


if __name__ == '__main__':
   app.run("127.0.0.1", 5000, debug=True)