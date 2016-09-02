from flask import Flask
from flask import jsonify, request, url_for
from . import api
from ..models import User, Todo, db
import json

@api.route('/')
def hello_world():
    return 'Flask Dockerized'


@api.route('/todos/')
def list_todos():
    todo_1 = Todo(1, 'Buy milk', 'Buy 2 of buttles of milk')
    todo_2 = Todo(2, 'Buy pork', 'Buy 2 kg. of pork')
    todo_3 = Todo(3, 'Learn python', 'Learn python programming')
    todos = Todo.query.all()
    return jsonify([each.to_json() for each in todos])


@api.route('/todos/<int:id>')
def get_todo(id):
    toto = Todo.query.get_or_404(id)
    response = jsonify(toto.to_json())
    response.add_etag()
    return response


@api.route('/todos/', methods=['POST'])
def create_todo():
    new_todo = Todo.from_json(request.json)
    db.session.add(new_todo)
    db.session.commit()

    return jsonify(), 201, \
           {'Location': url_for('api.get_todo', id=new_todo.id, _external=True)}


@api.route('/users/')
def get_user():
    user_songpon = User(1, 'Songpon', 't.songpon@gmail.com', 30)
    user_tum = User(2, 'Tum', 'tum@songpon.net', 25)
    users = [user_songpon, user_tum]
    return jsonify([each_user.to_json() for each_user in users])
