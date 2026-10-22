
from flask import Flask

app = Flask(__name__)

@app.route('/grade/<int:percentage>')
def grade(percentage):
    if percentage > 80:
        result = 'A Grade'
    elif percentage > 60:
        result = 'B Grade'
    elif percentage > 40:
        result = 'C Grade'
    else:
        result = 'Fail'

    return f'''
        <h2>Marks Percentage: {percentage}%</h2>
        <h2>Grade: {result}</h2>
    '''


@app.route('/students')
def students():
    student_list = [
        {'id': 1, 'name': 'Ravi', 'percentage': 92},
        {'id': 2, 'name': 'Sita', 'percentage': 85},
        {'id': 3, 'name': 'Jahnavi', 'percentage': 89},
        {'id': 4, 'name': 'Kiran', 'percentage': 76},
        {'id': 5, 'name': 'Priya', 'percentage': 81},
        {'id': 6, 'name': 'Rahul', 'percentage': 68},
        {'id': 7, 'name': 'Anu', 'percentage': 95},
        {'id': 8, 'name': 'Manoj', 'percentage': 54},
        {'id': 9, 'name': 'Divya', 'percentage': 73},
        {'id': 10, 'name': 'Sai', 'percentage': 40}
    ]

    output = '<h1>Student Records</h1><table border="1" cellpadding="10">'
    output += '<tr><th>ID</th><th>Name</th><th>Percentage</th></tr>'

    for student in student_list:
        output += f'''
            <tr>
                <td>{student['id']}</td>
                <td>{student['name']}</td>
                <td>{student['percentage']}%</td>
            </tr>
        '''

    output += '</table>'
    return output

if __name__ == '__main__':
    app.run(debug=True)
