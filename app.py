from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False

    for i in range(5, int(n**0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])

def calculate():
    birth_year = int(request.form['birthYear'])
    current_year = datetime.datetime.now().year
    age = current_year - birth_year

    next_prime_year = current_year
    
    while True:
        age += 1
        next_prime_year += 1
        
        if is_prime(age):
            break

    return {'next_prime_year': next_prime_year}

if __name__ == '__main__':
    app.run(debug=True)