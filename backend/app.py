from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
# Database file path
DATABASE = os.path.join(os.path.dirname(__file__), 'student.db')


# Helper function to execute SQL queries
def execute_query(query, args=(), fetch=False):
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row  # Use Row factory to return dictionaries
    cursor = connection.cursor()
    cursor.execute(query, args)
    if fetch:
        result = cursor.fetchall()
        result = [dict(row) for row in result]  # Convert rows to dictionaries
    else:
        connection.commit()
        result = None
    connection.close()
    return result

# Route to get all students
@app.route('/students', methods=['GET'])
def get_students():
    query = "Select student_index,FirstName,LastName, MajorName, GroupName from students s join majors m on s.MajorID=m.MajorID join groups g on s.GroupID = g.GroupID;"
    students = execute_query(query, fetch=True)
    return jsonify(students)

# Route to get a specific student by ID - Filtering
@app.route('/students/<int:student_index>', methods=['GET'])
def get_student(student_index):
    query = "Select student_index,FirstName,LastName, MajorName, GroupName from students s join majors m on s.MajorID=m.MajorID join groups g on s.GroupID = g.GroupID WHERE student_index = ?"
    student = execute_query(query, (student_index,), fetch=True)
    if student:
        return jsonify(student)
    else:
        return jsonify({"error": "Student not found"}), 404



# Route to get payments for a specific student
@app.route('/payments/<int:student_index>', methods=['GET'])
def get_student_payments(student_index):
    query = "Select PaymentDate, Amount from payments  WHERE student_index = ?"
    payments = execute_query(query, (student_index,), fetch=True)
    return jsonify(payments)


# Route to get total for a specific student
@app.route('/totals/<int:student_index>', methods=['GET'])
def get_student_total(student_index):
    query = "SELECT * FROM totals WHERE student_index = ?"
    total = execute_query(query, (student_index,), fetch=True)
    if total:
        return jsonify(total)
    else:
        return jsonify({"error": "Student not found"}), 404

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)