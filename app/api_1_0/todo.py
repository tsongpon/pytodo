from flask import jsonify, request, url_for
from . import api
from ..models import Todo, db


@api.route('/')
def hello_world():
    return 'Flask Dockerized'


@api.route('/todos/',  methods=['GET'])
def list_todos():
    return jsonify([each.to_json() for each in Todo.query.all()])


@api.route('/todos/<int:id>', methods=['GET'])
def get_todo(id):
    todo = Todo.query.get_or_404(id)
    response = jsonify(todo.to_json())
    response.add_etag()
    return response


@api.route('/todos', methods=['POST'])
def create_todo():
    new_todo = Todo.from_json(request.json)
    db.session.add(new_todo)
    db.session.commit()

    return '', 201, \
           {'Location': url_for('api.get_todo', id=new_todo.id, _external=True)}


@api.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return '', 200


@api.route('/todos/<int:id>', methods=['PUT'])
def update_todo(id):
    todo_from_db = Todo.query.get_or_404(id)
    todo_from_request = Todo.from_json(request.json)

    todo_from_db.task = todo_from_request.task
    todo_from_db.detail = todo_from_request.detail
    todo_from_db.is_done = todo_from_request.is_done

    db.session.commit()
    return '', 200

