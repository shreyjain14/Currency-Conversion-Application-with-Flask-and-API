from flask import Flask, render_template
from dotenv import load_dotenv
import os
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, IntegerField
from wtforms.validators import InputRequired
from convert import get_currencies, convert_currency

app = Flask(__name__)
load_dotenv('.env')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


class CurrencyConvert(FlaskForm):
    amount = IntegerField(validators=[InputRequired()])

    currencies = get_currencies()
    currency1 = SelectField(label='Currency From', choices=currencies, validators=[InputRequired()])
    currency2 = SelectField(label='Currency To', choices=currencies, validators=[InputRequired()])

    submit = SubmitField('Convert')


@app.route('/', methods=['GET', "POST"])
def home():
    form = CurrencyConvert()
    if form.validate_on_submit():
        amount = form.amount.data
        currency1 = form.currency1.data[0:3]
        currency2 = form.currency2.data[0:3]

        if currency1 == currency2:
            error = "ERROR: Please choose different currencies"
            return render_template('index.html', form=form, error=error)

        converted_amount = convert_currency(amount, currency1, currency2)
        converted_data = {
            'amount': amount,
            'currency1': currency1,
            'currency2': currency2,
            'converted_amount': converted_amount
        }
        return render_template('index.html', form=form, converted_data=converted_data)

    return render_template('index.html', form=form)


if __name__ == "__main__":
    app.run()
