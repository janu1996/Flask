
from flask import Flask, request, render_template_string

app = Flask(__name__)

# Signup form
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        address = request.form.get('address')
        password = request.form.get('password')

        return f'''
            <h2>Signup Successful!</h2>
            <p>Username: {username}</p>
            <p>Email: {email}</p>
            <p>Address: {address}</p>
            <p>Password received successfully.</p>
        '''

    return render_template_string('''
        <h2>Signup Form</h2>
        <form method="POST" action="/signup">
            <label>Username:</label>
            <input type="text" name="username" required>
            <br><br>

            <label>Email:</label>
            <input type="email" name="email" required>
            <br><br>

            <label>Address:</label>
            <textarea name="address" required></textarea>
            <br><br>

            <label>Password:</label>
            <input type="password" name="password" required>
            <br><br>

            <button type="submit">Sign Up</button>
        </form>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
