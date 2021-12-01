from flask import Flask, redirect, render_template, url_for

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

if __name__ == '__main__':
   app.run("127.0.0.1", 5000, debug=True)