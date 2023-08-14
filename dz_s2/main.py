# Создать страницу, на которой будет форма для ввода имени
# и электронной почты, при отправке которой будет создан
# cookie-файл с данными пользователя, а также будет произведено
# перенаправление на страницу приветствия, где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка «Выйти»,
# при нажатии на которую будет удалён cookie-файл с данными пользователя
# и произведено перенаправление на страницу ввода имени и электронной почты


from flask import Flask, render_template, make_response, request, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def start():
    response = make_response(render_template('form.html'))
    response.delete_cookie('name')
    response.delete_cookie('mail')
    if request.method == 'POST':
        username = request.form.get('human')
        email = request.form.get('email')
        response = make_response(redirect(url_for('hello')))
        response.set_cookie('name', username)
        response.set_cookie('mail', email)
        return response
    return render_template('form.html')


@app.route('/hello/')
def hello():
    context = {
        'name': request.cookies.get('name'),
        'mail': request.cookies.get('mail')
    }
    return render_template('hello.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
