from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return f'Welcome to Day-3 Learning about Static vs Dynamic route'
@app.route('/profile/')
def details():
    return f'Hii...This is Jahnavi'
#static routing --> /name/janu
#dynamic routing -->/name/<name>
@app.route('/name/janu') #static route
def data():
    return f'Welcome Jaanu...'
@app.route('/name/<name>') #url # dynamic route
def student_name(name): # endpoint with function & endpoint should not be same
    return f'Hello {name}'
#Now we want to create related to course names
@app.route('/courses/<course_name>')
def courses(course_name):
    return f'<b>This course is:{course_name} </b>'
#Multiple Routes to one view function
@app.route('/sir')
@app.route('/mam')
def check():
    return f'Welcome to Day-3 Learning about Static ns Dynamic routing'

#converters --> int,str,float,path,uuid
#Integer converters
@app.route('/students/<int:student_id>')
def studentid(student_id):
    return f'The ID of Student is {student_id}'
#Float Converters
@app.route('/percentages/<float:percentage>')
def stupercentages(percentage):
    return f'The students percentage is {percentage} good'
#Path converters
@app.route('/path/<path:file_name>')
def filepath(file_name):
    return f'The path is {file_name}'
#uuid converter
#UUID --> Universal Unique Identifier
@app.route('/student_id/<uuid:stu_id>')
def student_id(stu_id):
    return f'The Search for Student is {stu_id}'
if __name__=="__main__":
    app.run(host='0.0.0.0',  #4 bits beacuse of IPV4  
            port = 5000,debug=True)
