from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

tasks = []

@app.route('/')
def inicio():
    return render_template('index.html', tasks = tasks)

@app.route('/add', methods = ['GET', 'POST'])
def add():
    if request.method == 'POST':
        task_name = request.form['task']
        if task_name:
            tasks.append(task_name)
            return redirect(url_for('inicio'))
    
    return render_template('add.html')



@app.route('/delete/<int:task_id>', methods=['POST'])
def delete(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)# elimino la tarea en el índice task_id
    return redirect(url_for('inicio'))


if __name__ == '__main__':
    app.run(debug=True)