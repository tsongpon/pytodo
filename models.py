class User:
    def __init__(self, user_id, name, email, age):
        self.id = user_id
        self.name = name
        self.email = email
        self.age = age

    def to_json(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'email' : self.email,
            'age' : self.age
        }


class Todo:
    def __init__(self, id, task, detail):
        self.id = id
        self.task = task
        self.detail = detail
        self.is_done = False

    def to_json(self):
        return {
            'id' : self.id,
            'task' : self.task,
            'detail' : self.detail,
            'is_done' : self.is_done
        }
