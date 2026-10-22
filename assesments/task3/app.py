
from flask import Flask, url_for, request

app = Flask(__name__)

# Task 1: Home to About navigation using url_for()
@app.route('/')
def home():
    return f'''
        <h1>Home Page</h1>
        <a href="{url_for('about')}">Go to About Page</a>
    '''

@app.route('/about')
def about():
    return '''
        <h1>About Page</h1>
        <p>Welcome to the About Page!</p>
        <a href="/">Back to Home</a>
    '''


# Task 2: GET request to get name and batchno
@app.route('/student', methods=['GET'])
def student():
    return {
        'name': 'Jahnavi',
        'batchno': 'PFS-004'
    }


# Task 3: POST request to get name and skills from JSON
@app.route('/skills', methods=['POST'])
def skills():
    data = request.get_json()

    return {
        'name': data.get('name'),
        'skills': data.get('skills')
    }


if __name__ == '__main__':
    app.run(debug=True)
