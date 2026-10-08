from flask import Flask, render_template, url_for
import uuid

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('resume.html')

@app.route('/home')
def home_page():
    return render_template('resume.html')

# About page
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/subject/<string:subject>/<float:marks>')
def subject_marks(subject, marks):
    return f"""
    <h1>Subject Details</h1>
    <p>Subject: {subject}</p>
    <p>Marks: {marks}</p>
    """

@app.route('/subject/<string:subject>/uuid')
def subject_uuid(subject):
    generated_uuid = uuid.uuid4()

    return f"""
    <h1>Subject UUID</h1>
    <p>Subject: {subject}</p>
    <p>UUID: {generated_uuid}</p>
    """


if __name__ == '__main__':
    app.run(debug=True)