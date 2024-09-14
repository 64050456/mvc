from flask import Flask, render_template, request, redirect, url_for
from dbset import db  
from data import Cow  

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

@app.route('/')
def index():
    cows = Cow.query.all()  
    return render_template('index.html', cows=cows)

@app.route('/calculate', methods=['POST'])
def calculate():
    cow_code = request.form['code']
    cow = Cow.query.filter_by(code=cow_code).first()  
    if cow:
        milk, flavor = cow.calculate_milk()  
        return render_template('result.html', cow=cow, milk=milk, flavor=flavor)
    else:
        return render_template('not_found.html', code=cow_code)

if __name__ == '__main__':
    app.run(debug=True)
