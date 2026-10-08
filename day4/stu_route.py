from flask import Flask
import uuid
app = Flask(__name__)
#Task 1
# Build a Student routing app
#Student default page
#Student id - dynamic
#Student attendence
#file path
#student uuid

@app.route('/')
def  home():
    return "Welcom to Student Routing Application"

@app.route('/students/<int:student_id>')
def studentid(student_id):
    return f'The ID of Student is {student_id}'

@app.route('/students/<float:student_att>')
def studentatt(student_att):
    return f'Student Attendence is :{student_att}'

@app.route('/skills/<s1>/<s2>')
def skills(s1,s2):
    return f'Student has {s1} and {s2} skills.'

@app.route('/path/<path:file_name>')
def filepath(file_name):
    return f'The path is {file_name}'

@app.route('/generate')
def generate():
    id = uuid.uuid4()
    return f'The student search  id is:{id}'

if __name__ == "__main__":
    app.run(host='0.0.0.0',
            port = 5000,debug=True)