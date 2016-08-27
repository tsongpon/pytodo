from flask import Flask
from flask import jsonify
from models import User, Todo
import json
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Flask Dockerized'

@app.route('/todos/')
def list_todos():
    todo_1 = Todo(1, 'Buy milk', 'Buy 2 of buttles of milk')
    todo_2 = Todo(2, 'Buy pork', 'Buy 2 kg. of pork')
    todos = [todo_1, todo_2]
    return jsonify([each.to_json() for each in todos])

@app.route('/users/')
def get_user():
    user_songpon = User(1, 'Songpon', 't.songpon@gmail.com', 30)
    user_tum = User(2, 'Tum', 'tum@songpon.net', 25)
    users = [user_songpon, user_tum]
    return jsonify([each_user.to_json() for each_user in users])

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
