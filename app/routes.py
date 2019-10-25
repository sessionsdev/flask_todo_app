from flask import current_app as app
from . import db
from flask import jsonify, render_template, request, redirect, url_for
from pony.orm import *
from .models import ToDoItem
import json
from .forms import AddTaskForm



#homepage
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = AddTaskForm()
    tasks = select(t for t in db.ToDoItem)
    if form.validate_on_submit():
        with db_session:
            task = db.ToDoItem(item=form.item.data, due_date=form.due_date.data)
            return redirect(url_for('index'))
    return render_template('index.html', tasks=tasks, form=form)




@app.route('/todo/tasks', methods = ['GET'])
def get_task():
    with db_session:
        return {
            item.id: {
                'task': item.item,
                'due date': item.due_date
            }
            for item in db.ToDoItem.select()
        }


@db_session
@app.route('/todo/tasks', methods=['POST'])
def add_task():
    r = request.get_json()
    item = r['item']
    due_date = r['due_date']
    task = db.ToDoItem(item=item, due_date=due_date)

    return "201"


@db_session
@app.route('/completed/<string:id>', methods=['GET', 'POST', 'DELETE'])
def remove_task(id):
    x = db.ToDoItem[id]
    x.delete()
    return redirect(url_for('index'))

