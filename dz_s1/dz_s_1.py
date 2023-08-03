# Создать базовый шаблон для интернет-магазина,
# содержащий общие элементы дизайна (шапка, меню, подвал),
# и дочерние шаблоны для страниц категорий товаров и отдельных товаров.
# Например, создать страницы «Одежда», «Обувь» и «Куртка», используя базовый шаблон.

from flask import Flask
from flask import render_template
from dataclasses import dataclass

app = Flask(__name__)


@app.route('/')
def about_us():
    return render_template("about_store.html")


@dataclass
class Contact:
    department: str
    number: str
    email: str = ''


contact_list = [
    Contact('Техническая поддержка', '+7 800 500 00 00', 'hotline@my_shop.ru'),
    Contact('Пункт выдачи заказов', '+7 555 333 77 77'),
    Contact('Отдел по сотрудничеству', '+7 555 222 77 22', 'сooperation@my_shop.ru'),
]


@app.route('/store_contacts/')
def store_contacts():
    return render_template("store_contacts.html", contacts=contact_list)


@app.route('/clothes/')
def clothes():
    return render_template("clothes.html")


@app.route('/clothes/outerwear/')
def outerwear():
    return render_template("outerwear.html")

@app.route('/clothes/outerwear/item_1/')
def outerwear_i_1():
    return render_template("item_1.html")


@app.route('/clothes/dresses/')
def dresses():
    return render_template("dresses.html")


@app.route('/shoes/')
def shoes():
    return render_template("shoes.html")


if __name__ == '__main__':
    app.run(debug=True)
