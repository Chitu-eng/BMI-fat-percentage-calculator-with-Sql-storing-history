from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bmi_data.db'
db = SQLAlchemy(app)

class BMIEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    weight = db.Column(db.Float, nullable=False)
    height = db.Column(db.Float, nullable=False)
    bmi = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), nullable=False)
    body_fat = db.Column(db.Float)          # new
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)



@app.route('/')
def home():
    return "Hello, world! Your health project is running."

@app.route('/bmi', methods=['GET', 'POST'])
def bmi():
    bmi_value = None
    status = None
    body_fat = None

    if request.method == 'POST':
        weight = float(request.form['weight'])
        height_cm = float(request.form['height'])
        height_m = height_cm / 100
        age = int(request.form['age'])
        gender = request.form['gender']  # "male" or "female"

        bmi_value = round(weight / (height_m ** 2), 2)

        if bmi_value < 18.5:
            status = "Underweight"
        elif bmi_value < 25:
            status = "Normal"
        elif bmi_value < 30:
            status = "Overweight"
        else:
            status = "Obese"

        # Body fat % using BMI method (adult)
        if gender == 'male':
            body_fat = 1.20 * bmi_value + 0.23 * age - 16.2
        else:  # female
            body_fat = 1.20 * bmi_value + 0.23 * age - 5.4

        body_fat = round(body_fat, 1)

        # Save in DB if you like (extend your BMIEntry model later to store age, gender, body_fat)

        entry = BMIEntry(
            weight=weight,
            height=height_m,
            bmi=bmi_value,
            status=status,
            body_fat=body_fat
            )           

        
        db.session.add(entry)
        db.session.commit()

    return render_template('bmi.html', bmi=bmi_value, status=status, body_fat=body_fat)


@app.route('/history')
def history():
    entries = BMIEntry.query.order_by(BMIEntry.timestamp.desc()).all()
    return render_template('history.html', entries=entries)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()   # creates tables only if they don't exist
    app.run(debug=True)
