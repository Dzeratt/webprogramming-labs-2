from flask import Flask, redirect, url_for, render_template
from lab1 import lab1

app = Flask(__name__)
app.register_blueprint(lab1)

@app.route('/lab2/example')
def example():
     name, lab_number, group, course = 'Денис Духов', 2, 'ФБИ-13', '3 курс'
     fruits = [
               {'name': 'яблоки', 'price': 100},
               {'name': 'груши', 'price': 120},
               {'name': 'апельсины', 'price': 80},
               {'name': 'мандарины', 'price': 95},
               {'name': 'манго', 'price': 321}
    ]
     books = [
               {'name': 'Улисс', 'author': 'Джеймс Дж.', 'pages': 1056, 'genre': 'Роман'},
               {'name': 'Трилогия желания', 'author': 'Драйзер Т.', 'pages': 1152, 'genre': 'Роман'},
               {'name': 'Война и мир', 'author': 'Толстой Л.', 'pages': 1360, 'genre': 'Роман-эпопея'},
               {'name': 'Сага о Форсайтах', 'author': 'Голсуорси Дж.', 'pages': 1376, 'genre': 'Роман'},
               {'name': 'Архипелаг ГУЛАГ', 'author': 'Солженицын А.', 'pages': 1424, 'genre': 'Исследования'},
               {'name': 'Квинканкс', 'author': 'Палиссер Ч.', 'pages': 1472, 'genre': 'Роман'},
               {'name': 'Иосиф и его братья', 'author': 'Манн Т.', 'pages': 1492, 'genre': 'Эпический роман'},
               {'name': 'Человек без свойств', 'author': 'Музиль Р.', 'pages': 1774, 'genre': 'Роман'},
               {'name': 'В поисках утраченного времени', 'author': 'Пруст М.', 'pages': 3031, 'genre': 'Роман'},
               {'name': 'Моя борьба', 'author': ' Кнаусгор К.', 'pages': 3600, 'genre': 'Роман'},
    ]
     return render_template('example.html', name=name, lab_number = lab_number, group =group, course=course, fruits=fruits, books=books)

@app.route('/lab2/')
def lab2():
          return render_template('lab2.html')
@app.route('/lab2/cars')
def cars():
          return render_template('cars.html')