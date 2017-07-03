# -*- coding: UTF-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import Pagination

app = Flask(__name__)
# mysql://username:password@server:port/db
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://fleeter:hust201417@182.254.230.24/fleeting'
app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', True)
# 设置自动提交数据库更改
app.config.setdefault('SQLALCHEMY_COMMIT_ON_TEARFDOWN', True)
db = SQLAlchemy(app)


# 定义User对象:
class User(db.Model):
    __tablename__ = 'fl_video'
    # 表的结构
    id = db.Column(db.SmallInteger, primary_key=True)
    title = db.Column(db.String(255), unique=True)
    cover = db.Column(db.String(1023), unique=True)
    description = db.Column(db.String(255))
    info = db.Column(db.String(255), nullable=True)
    url = db.Column(db.String(10000))
    upload_time = db.Column(db.DateTime)
    size = db.Column(db.SmallInteger)
    duration = db.Column(db.Integer, nullable=True)
    type = db.Column(db.String(25))

    def __init__(self, title, cover, description, info, url, upload_time, size, duration, type):
        self.title = title
        self.cover = cover
        self.description = description
        self.info = info
        self.url = url
        self.upload_time = upload_time
        self.size = size
        self.duration = duration
        self.type = type

    # __repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的
    def __repr__(self):
        return str({
            "title": self.title,
            "cover": self.cover,
            "description": self.description,
            "info": self.info,
            "url": self.url,
            "upload_time": self.upload_time,
            "size": self.size,
            "duration": self.duration,
            "type": self.type
        })


db.create_all()
a = User.query.filter(User.url)
print(a)

