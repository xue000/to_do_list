from flask import flash, redirect, url_for, render_template
from app import app, db
from app.models import Task, Admin
from app.forms import TaskForm, LoginForm
from flask_login import login_user, logout_user, login_required, fresh_login_required, current_user
from app.utils import redirect_back

#the index page
@app.route('/', methods=['GET', 'POST'])
def index():
    if current_user.is_authenticated:
        return redirect(url_for('menu'))

    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        admin = Admin.query.first()
        if admin:
            if username == admin.username and admin.validate_password(password):
                login_user(admin)
                flash('Welcome back.', 'info')
                return redirect_back()
            flash('Invalid username or password.', 'warning')
        else:
            flash('No account.', 'warning')
    return render_template('index.html', form=form)

@app.route("/menu")
@login_required
def menu():
        return render_template('menu.html',
                               title='homepage',
                             )

#the create task
@app.route('/create_task', methods=['GET','POST'])
@login_required
def create_task():
    form = TaskForm()
    flash('Errors="%s"' %
          (form.errors))
    if form.validate_on_submit():
        t = Task(title = form.title.data, description = form.description.data, date= form.date.data)
        db.session.add(t)
        db.session.commit()
        return redirect('/task')
    return render_template('create_task.html',
                           title='Create Task',
                           form=form)

#the task list
@app.route('/task', methods=['GET'])
@login_required
def getAllTasks():
    #get all the task
    tasks = Task.query.all()
    return render_template('task_list.html',
                           title='All Task',
                           tasks=tasks)

#the completed tasks list
@app.route('/completed_tasks', methods=['GET'])
@login_required
def getAllCompletedTasks():
    tasks = Task.query.all()
    return render_template('completed_task_list.html',
                           title='All Completed Task',
                           tasks=tasks)

#the uncompleted task list
@app.route('/uncompleted_tasks', methods=['GET'])
@login_required
def getAllUncompletedTasks():
    tasks = Task.query.all()
    return render_template('uncompleted_task_list.html',
                           title='All Uncompleted Task',
                           tasks=tasks)

#to edit the task
@app.route('/edit_task/<id>', methods=['GET','POST'])
@login_required
def edit_task(id):
    task = Task.query.get(id)
    form = TaskForm(obj=task)
    flash('Errors="%s"' %
          (form.errors))
    if form.validate_on_submit():
        t = task
        t.title = form.title.data
        t.description = form.description.data
        t.date = form.date.data
        db.session.commit()
        return redirect('/task')
    return render_template('edit_task.html',
                           title='Edit Task',
                           form=form)

#to delete the task
@app.route('/delete_task/<id>', methods=['GET'])
@login_required
def delete_task(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return redirect('/task')

#change the status of the task to completed
@app.route('/finish_task/<id>', methods=['GET','POST'])
@login_required
def Finish_task(id):
    task = Task.query.get(id)
    task.status = "Completed"
    db.session.commit()
    return redirect('/task')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout success.', 'info')
    return redirect('')
