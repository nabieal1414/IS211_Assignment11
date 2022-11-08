from flask import Blueprint, render_template
from controllers.todoController import index, add_todo, clear_todos, delete_todo

todo_bp = Blueprint('todo_bp', __name__,  template_folder='templates')

todo_bp.route('/', methods=['GET'])(index)
todo_bp.route('/submit', methods=['POST'])(add_todo)
todo_bp.route('/clear', methods=['POST'])(clear_todos)
todo_bp.route('/delete/<id>', methods=['POST'])(delete_todo)