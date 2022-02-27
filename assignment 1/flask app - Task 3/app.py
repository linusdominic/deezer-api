from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', todo_list=todo_list)

@app.route('/add-todo', methods=['POST'])
def addTodo():
    todo = request.form['todo']
    todo_list.append(todo)
    return render_template('index.html', todo_list=todo_list)

@app.route('/delete/<int:todo>')
def deleteTodo(todo):
    todo_list.pop(todo)
    return render_template('index.html', todo_list=todo_list)


if __name__ == '__main__':
    todo_list = []
    app.run(host='0.0.0.0', port=8080, debug=False)