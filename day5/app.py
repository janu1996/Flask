from flask import Flask,redirect,render_template,url_for,request
#create a flask application instance
app = Flask(__name__)

@app.route('/')
def home():
    #return f'Flask Server is running'
    return render_template('index.html')

#name = Jahnavi,email = jahnavisaidevi@gmail.com
@app.route('/getData',methods=['GET'])
def getData():
    name = request.args.get('name')
    email = request.args.get('email')
    return f'The name is {name} and email is {email}'
'''
@app.route('/getDataformPOST',methods=['POST'])
def getDatafromPOST():
    data = request.get_json()
    name = data['name']
    email = data['email']
    return f'Then name is {name} and eamil is {email}'
'''
@app.route('/postData',methods=['POST'])
def postData():
    name = request.form['name']
    email = request.form['email']
    password =request.form['password']
    if name is None or len(name) < 5:
        return render_template('index.html',
                               err='Invalid name')
    if email is None:
        return render_template('index.html',
                               err='Invail email')
    if password is None or len(password) < 4:
        return render_template('index.html',
                               err="password doesnot match")
    return render_template('index.html',
                           msg ='Successful')
    
if __name__ == "__main__":
    app.run(debug=True)