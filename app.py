from flask import Flask, jsonify
import flask_restful
from flask import abort
from flask import make_response
from flask import request

from models.recommend_list import RecommendList
from models.sorted_list import SortedList
from models.log_in import Login
from models.collection import Collection

app = Flask(__name__)
api = flask_restful.Api(app)
# mysql://username:password@server:port/db

# app.config.from_pyfile('config/test.cfg')
# db = SQLAlchemy(app)
# from orm.fl_video import User
# db.create_all()



class HelloWorld(flask_restful.Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/')
# 返回推荐列表
api.add_resource(RecommendList, "/fleeting/api/v1.0/recommendlist")
# 返回分类列表
api.add_resource(SortedList, "/fleeting/api/v1.0/sortedlist", "/fleeting/api/v1.0/sortedlist/<string:video_type>")
# 用户登录注册
api.add_resource(Login, "/fleeting/api/v1.0/user/<string:type>")
# 用户登录后返回收藏夹信息
api.add_resource(Collection, "/fleeting/api/v1.0/user/collection/<string:username>")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


'''
tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }]


@app.route('/')
def index():
    return 'Hello,world!'


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = filter(lambda t: t['id'] == task_id, tasks)
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})


@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or 'title' not in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

'''
