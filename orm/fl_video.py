# -*- coding: UTF-8 -*-
# import os
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

from app import db
from flask_restful import Resource


# 定义User对象:
class User(db.Model, Resource):
    # 设置表名
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

    def get(self):
        video_obj = self.query.all()
        for i in range(len(video_obj)):
            self.video_list.append({
                "title1": video_obj[i].title,
                "cover": video_obj[i].cover,
                "description": video_obj[i].description,
                "info": video_obj[i].info,
                "url": video_obj[i].url,
                "upload_time": video_obj[i].upload_time,
                "size": video_obj[i].size,
                "duration": video_obj[i].duration,
                "type": video_obj[i].type
            })
        return self.video_list

        # __repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的
        # def __repr__(self):
        #     return str({
        #         "title1": self.title,
        #         "cover": self.cover,
        #         "description": self.description,
        #         "info": self.info,
        #         "url": self.url,
        #         "upload_time": self.upload_time,
        #         "size": self.size,
        #         "duration": self.duration,
        #         "type": self.type
        #     })


a = User.query.filter_by(type="动画短片").first()
print(a)
