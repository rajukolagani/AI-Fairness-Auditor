from flask import Flask, render_template, request
import pandas as pd
# We will create auditor.py in the next step
from auditor import audit_model

# Initialize the Flask app
app = Flask(__name__)

# --- Load data to get column names for the dropdown menu ---
# This runs only once when the app starts.
try:
    df = pd.read_csv('data/adult.csv')
    # We only want to audit specific categorical columns
    AUDITABLE_COLUMNS = [col for col in ['gender', 'race', 'relationship', 'workclass'] if col in df.columns]
except FileNotFoundError:
    print("ERROR: adult.csv not found. Please run prepare_data.py first.")
    AUDITABLE_COLUMNS = []

# --- Define the routes (the different pages of the web app) ---

# This is the main page (e.g., http://127.0.0.1:5000)
@app.route('/')
def index():
    """Renders the main page with the form."""
    # Pass the list of columns to the HTML so it can build the dropdown menu
    return render_template('index.html', columns=AUDITABLE_COLUMNS)

# This route handles the form submission
@app.route('/audit', methods=['POST'])
def audit():
    """Handles the form submission and displays the results."""
    # Get the attribute the user selected from the form
    selected_attribute = request.form['attribute']

    # Make sure the selected attribute is valid
    if selected_attribute not in AUDITABLE_COLUMNS:
        return "Error: Invalid attribute selected.", 400

    # Call the audit_model function from auditor.py to do the analysis
    results = audit_model(selected_attribute)

    # Send the results to the results.html page to be displayed
    return render_template('results.html', results=results)

# --- This part runs the app ---
if __name__ == '__main__':
    # debug=True means the server will auto-reload when you save changes
    app.run(debug=True)