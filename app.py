
from forex_python.converter import CurrencyRates, CurrencyCodes
from flask import Flask, request, render_template, session, url_for, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
import requests

app = Flask(__name__)

app.config['SECRET_KEY'] = "cheese"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


@app.route('/')
def index():
    """Shows home page of application."""

    return render_template('index.html')

c = CurrencyCodes()
rate = CurrencyRates()

@app.route('/conversion', methods=[ 'POST'])
def conversion():
    
    convert_from = request.form['convert_from'].upper()
    convert_to = request.form['convert_to'].upper()
    amount = request.form['amount']
    symbol1 = c.get_symbol(convert_from)
    symbol2 = c.get_symbol(convert_to)
    example = rate.convert('USD', 'EUR', 5)

    if c.get_currency_name(convert_from) == "None":
        flash("Please enter a valid currency")
        
        if c.getcurrency_name(convert_to) == "None":
            flash("Please enter a valid currency")
        
        if amount < 0:
            flash("Not a vaild amount")
        
        return redirect('/')

    else:
        url = (f"https://api.exchangerate.host/convert?from={convert_from}&to={convert_to}&amount={amount}&symbols={convert_to}&places=2")
        response = requests.get(url)
        data = response.json()

        flash(example)
        return render_template('result.html', data=data, convert_from=convert_from, convert_to=convert_to, amount=amount, symbol1=symbol1, symbol2=symbol2 example=example)

    
   
