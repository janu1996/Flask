
from flask import Flask, url_for, request

# Create Flask application first
app = Flask(__name__)

# Task 1: Home to About navigation using url_for
@app.route('/')
def home():
    return f'''
        <h1>Home Page</h1>
        <a href="{url_for('about')}">Go to About Page</a>
    '''

@app.route('/about')
def about():
    return '<h1>Welcome to About Page</h1>'


# Task 2: GET request for name and batch number
@app.route('/student', methods=['GET'])
def get_student():
    return {
        'name': 'Jahnavi',
        'batchno': 'BATCH101'
    }


# Task 3: POST request for name and skills
@app.route('/skills', methods=['POST'])
def get_skills():
    data = request.get_json()

    return {
        'name': data.get('name'),
        'skills': data.get('skills')
    }


# Run the application at the end
if __name__ == '__main__':
    app.run(debug=True)
