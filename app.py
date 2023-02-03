from flask import Flask, request, jsonify

app = Flask(__name__)

# A sample data store
employees = [
    {
        'id': 1,
        'name': 'John Doe',
        'salary': 50000
    },
    {
        'id': 2,
        'name': 'Jane Doe',
        'salary': 55000
    }
]

@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employees)

@app.route('/employees', methods=['POST'])
def create_employee():
    employee = request.get_json()
    employee['id'] = len(employees) + 1
    employees.append(employee)
    return jsonify(employee), 201

@app.route('/employees/<int:employee_id>', methods=['GET'])
def get_employee(employee_id):
    employee = next((e for e in employees if e['id'] == employee_id), None)
    if employee is None:
        return 'Employee not found', 404
    return jsonify(employee)

@app.route('/employees/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    employee = next((e for e in employees if e['id'] == employee_id), None)
    if employee is None:
        return 'Employee not found', 404
    update = request.get_json()
    employee.update(update)
    return jsonify(employee)

@app.route('/employees/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    employee = next((e for e in employees if e['id'] == employee_id), None)
    if employee is None:
        return 'Employee not found', 404
    employees.remove(employee)
    return '', 204

if __name__ == '__main__':
    app.run()