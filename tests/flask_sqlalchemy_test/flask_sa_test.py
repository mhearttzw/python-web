from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root: @localhost/test'
app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', True)
# 设置自动提交数据库更改
app.config.setdefault('SQLALCHEMY_COMMIT_ON_TEARFDOWN', True)
db = SQLAlchemy(app)

# 定义User对象:
class User(db.Model):
    __tablename__ = 'user'
    # 表的结构
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    # email = db.Column(db.String(120), unique=True)

    # def __init__(self, username, email):
    #     self.username = username
    #     # self.email = email

    # __repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的
    def __repr__(self):
        return '<User %r>' % self.name


print(User.query.all())
