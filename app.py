from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    task_content = request.form.get('task')
    tasks.append(task_content)
    return jsonify({'message': 'Task added successfully'})

@app.route('/update_task/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    new_content = request.form.get('new_content')
    tasks[task_id] = new_content
    return jsonify({'message': 'Task updated successfully'})

@app.route('/delete_task/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    del tasks[task_id]
    return jsonify({'message': 'Task deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
