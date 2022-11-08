from flask import render_template, request, redirect
import re
import uuid
import pickle

todos = []

def index():
    return render_template('index.html', todos=todos)

def add_todo():
    task = request.form['task']
    email = request.form['email']
    priority = request.form['priority']
    errors=[]
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
    if task == '':
        errors.append('Task field cannot be empty')
    if email == '':
        errors.append('Email field cannot be empty')
    elif not re.search(regex, email):
        errors.append('Email is invalid')
    
    if len(errors) > 0:
        return redirect('/?error='+','.join(errors), code=302)
    todos.append({'id': uuid.uuid1(), 'task': task, 'email': email, 'priority': priority})
    
    return redirect("/", code=302)

def clear_todos():
    todos.clear()
   
    return redirect('/', code=302)

def delete_todo(id):
    for todo in todos:
        if str(todo['id']) == id:
            todos.remove(todo)
            break
    
    return redirect('/', code=302)
