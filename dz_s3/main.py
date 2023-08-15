# Создать форму для регистрации пользователей на сайте.
# Форма должна содержать поля "Имя", "Фамилия", "Email", "Пароль"
# и кнопку "Зарегистрироваться". При отправке формы
# данные должны сохраняться в базе данных, а пароль должен быть зашифрован.


from dz_s3.models import db, User
from flask import Flask, render_template, request
from dz_s3.forms import RegisterForm
from flask_wtf.csrf import CSRFProtect
from dz_s3.encrypt import encrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SECRET_KEY'] = b'n837tb4r8cq8473yr8q2yn398rynq0cny3r8c7ynq98c347ytn8yebuwfgr'
csrf = CSRFProtect(app)

db.init_app(app)


@app.route('/')
def index():
    return 'db user!'


@app.cli.command("init-db")
def init_db():
    db.create_all()


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        name = form.name.data
        surname = form.surname.data
        date_birth = form.date_birth.data
        email = form.email.data
        password = encrypt(form.password.data)
        existing_user = User.query.filter((User.name == name) | (User.email == email)).first()
        if existing_user:
            error_msg = 'Username or email already exists.'
            form.name.errors.append(error_msg)
            return render_template('register.html', form=form)
        user = User(name=name, surname=surname, date_birth=date_birth, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return 'Registration success!'
    return render_template('register.html', form=form)


@app.route('/check/')
def get():
    users = User.query.all()
    return render_template('users.html', users=users)


if __name__ == '__main__':
    app.run(debug=True)
