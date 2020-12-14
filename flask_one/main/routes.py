from flask import Blueprint,render_template,url_for
import os
from flask_one.extensions import mongo

main = Blueprint('main',__name__)

@main.route('/')
def index():
    todo_collection = mongo.db.todo
    todos = todo_collection.find()
    return render_template('index.html',todos=todos)
    todo_collection.delete_one({'_id':ObjectId(oid)})
