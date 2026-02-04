# BMI-fat-percentage-calculator-with-Sql-storing-history

```markdown
# BMI & Body Fat Tracker (Flask)

A web-based health tracker that calculates BMI, classifies weight status, estimates body fat percentage, and stores each entry in a SQLite database with a history view.[file:13] This project was developed as a group project by a team of three members.[file:13]

## Features

- BMI calculation from weight and height (metric units).[file:13]  
- Weight status classification: Underweight, Normal, Overweight, Obese.[file:13]  
- Body fat percentage estimation using BMI, age, and gender (male/female).[file:13]  
- Persistent storage of entries (weight, height, BMI, status, body fat, timestamp) in SQLite.[file:13]  
- `/bmi` page: form input and result display using `bmi.html` template.[file:13][file:12]  
- `/history` page: table of past BMI entries with latest first using `history.html`.[file:13][file:11]  
- Simple landing route (`/`) confirming that the health project is running.[file:13]

## Requirements

- Python 3.8+ (recommended).[file:13]

### Python modules

Install the required modules:

```bash
pip install flask flask_sqlalchemy
```

Standard library modules used (no extra install): `datetime`.[file:13]

## Project Structure

- `app.py` – Main Flask application, routes, and database models.[file:13]  
- `bmi.html` – Template for BMI form and results page.[file:12]  
- `history.html` – Template to display saved BMI entries.[file:11]  
- `style.css` – Styles for the HTML templates.[file:14]  
- `bmi_data.db` – SQLite database file created automatically on first run.[file:13]

## Setup & Usage

1. Clone this repository and navigate into the project directory.
2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install flask flask_sqlalchemy
   ```

4. Run the app:

   ```bash
   python app.py
   ```

5. Open your browser and visit:

   - `http://127.0.0.1:5000/bmi` to calculate BMI and body fat.
   - `http://127.0.0.1:5000/history` to view your saved history.[file:13]

## Project Context

This health-focused web application was built collaboratively by a three-person team as a learning project in web development and databases.[file:13] The goal was to combine **Flask**, SQLAlchemy, and basic health formulas into a simple tool that tracks changes in BMI and body fat over time.[file:13]
```
