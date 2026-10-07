from flask import Flask
#create a Flask application instance
app = Flask(__name__)
#now we will start defining the routes
@app.route('/')
def home():
    """Default home page"""
    return "Hello Welcome to Flask Session Day-2"
@app.route('/jahnavi')
def detalis():
    """Details about Jahnavi"""
    return "Jahnavi is a Python Full Stack Trainne at Codegnan,Vizag"
@app.route('/students')
def data():
    """Students info"""
    return "Students are from Codegnan"
@app.route('/profile')
def profile():
    """About Jahnavi"""
    return "Jahnavi belongs to PFS-VSP-004 Batch"
if __name__ == "__main__":
    #if port is already in use change the port
    app.run(host='0.0.0.0',
            port=5500,debug=True)

