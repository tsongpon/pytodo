from . import db


class User:
    def __init__(self, user_id, name, email, age):
        self.id = user_id
        self.name = name
        self.email = email
        self.age = age

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'age': self.age
        }


class Todo(db.Model):
    __tablename__ = 'todo'

    def __init__(self, id, task, detail):
        self.id = id
        self.task = task
        self.detail = detail
        self.is_done = False

    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(128))
    detail = db.Column(db.String(1000))
    is_done = db.Column(db.Boolean)

    def to_json(self):
        return {
            'id': self.id,
            'task': self.task,
            'detail': self.detail,
            'is_done': self.is_done
        }

    @staticmethod
    def from_json(json):
        id = json.get('id')
        task = json.get('task')
        detail = json.get('detail')
        is_done = json.get('is_done')
        todo = Todo(id, task, detail)
        todo.is_done = is_done

        return todo
