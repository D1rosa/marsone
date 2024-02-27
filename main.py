from datetime import datetime
from flask import Flask, render_template, redirect, request, make_response, session, abort
from data import session
from data.users import User
from data.jobs import Jobs
# from forms.news import NewsForm
# from forms.user import RegisterForm, LoginForm
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


def main():
    session.global_init("db/blogs.db")
    # app.run()
    user = User()
    user.name = "Ridley"
    user.about = "Scott"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    db_sess = session.create_session()
    db_sess.add(user)
    job = Jobs()
    job.team_leader = 1
    job.job = "deployment of residential modules 1 and 2"
    job.age = 21
    job.work_size = 15
    job.collaborators = "2, 3"
    job.start_date = datetime.now()
    job.is_finished = False
    db_sess = session.create_session()
    db_sess.add(job)
    db_sess.commit()

