from flask import Flask, render_template, request
from next_prime_calculator import get_next_prime_year


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    birth_year = int(request.form['birthYear'])
    next_prime_year = get_next_prime_year(birth_year)

    return {'next_prime_year': next_prime_year}

if __name__ == '__main__':
    app.run(debug=True)
