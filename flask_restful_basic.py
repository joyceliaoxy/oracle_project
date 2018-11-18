from flask import Flask, request
from flask_restful import Resource, Api, reqparse, abort

# restful Api
app = Flask(__name__)
api = Api(app)

todo = {
    'todo1': {'task': 'build api'},
    'todo2': {'task': 'say hello'},
    'todo3': {'task': 'done!'},
}

def todo_is_none(todo_id):
    if todo_id not in todo:
        abort(404, message = "Todo {} dosen't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task')

# shows a single todo item and can delete a todo item
class Todo(Resource):
    def get(self, todo_id):
        todo_is_none(todo_id)
        return todo[todo_id]

    def delete(self, todo_id):
        del todo[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        todo[todo_id] =task
        return task,201

    def post(self):
        some_json = request.get_json()
        return {'you sent': some_json}, 201

# shows a list of all todos, and can post to add new task
class Todo_list(Resource):
    def get(self):
        return todo

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(todo.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        todo[todo_id] = {'task': args['task']}
        return todo[todo_id], 201

class Multi(Resource):
    def get(self, num):
        return {'result': num * 10}

api.add_resource(Todo, '/todos/<todo_id>')
api.add_resource(Todo_list, '/todos')
api.add_resource(Multi, '/multi/<int:num>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
