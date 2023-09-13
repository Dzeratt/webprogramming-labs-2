from flask import Flask, redirect, url_for
app = Flask(__name__)
@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)

@app.route("/menu")
def menu():
    return '''
        <!doctype html>
        <html>
            <head>
                <title>НГТУ, ФБ, Лабораторные работы</title>
                <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
            </head>
            <body>
                <header class="header">
                    НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
                </header>

                <main>
                    <ol>
                    <li>
                        <a href="/lab1" target="_blank">Лабораторная работа 1</a>
                    </li>
                    <ol>
                </main>

                <footer class="footer">
                    &copy; Духов Д.Ю., ФБИ-13, 3 курс, 2023
                </footer>
            </body>
        </html>    
    '''      

@app.route("/lab1")
def lab1():
        return '''
    <!doctype html>
    <html>
        <head>
            <title>Духов Денис Юрьевич, лабораторная 1</title>
            <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
        </head>
        <body>
            <header class="header">
                НГТУ, ФБ, Лабораторная работа 1
            </header>

            <h1>web-сервер на flask</h1>

            <div>
                Flask — фреймворк для создания веб-приложений на языке
                программирования Python, использующий набор инструментов
                Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
                называемых микрофреймворков — минималистичных каркасов
                веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
            </div>

            <a href="/menu" target="_blank">Меню</a>

            <h2>Реализованные роуты</h2>

            <ol>
                <li>
                    <a href="/lab1/oak" target="_blank">/lab1/oak - дуб</a>
                </li>
                <li>
                    <a href="/lab1/student" target="_blank">/lab1/student - студент</a>
                </li>
                <li>
                    <a href="/lab1/python" target="_blank">/lab1/python - python</a>
                </li>
                <li>
                    <a href="/lab1/something" target="_blank">/lab1/something - что-то</a>
                </li>
            </ol>

            <footer class="footer">
                &copy; Духов Д.Ю., ФБИ-13, 3 курс, 2023
            </footer>
        </body>
    </html>    
'''

@app.route('/lab1/oak')
def oak():
     return '''
   <!doctype html>
    <html>
        <head>
            <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
        </head>
        <body>
            <h1 id="page_name">Дуб</h1>
            <div id="style_oak">
                <img src="''' + url_for('static', filename='oak.jpg') + '''">
            </div>
        </body>
    </html>   
'''

@app.route('/lab1/student')
def student():
     return '''
   <!doctype html>
    <html>
        <head>
            <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
        </head>
        <body>
            <h1 id="page_name">Духов Денис Юрьевич</h1>
            <div id="style_nstu">
                <img src="''' + url_for('static', filename='Логотип_НГТУ_НЭТИ.png') + '''">
            </div>
        </body>
    </html>   
'''
@app.route('/lab1/python')
def python():
     return '''
   <!doctype html>
    <html>
        <head>
            <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1.css') + '''">
        </head>
        <body>
            <div class="phyton_txt">
                Python — это скриптовый язык программирования. 
                Он универсален, поэтому подходит для решения разнообразных 
                задач и для многих платформ: начиная с iOS и Android и заканчивая 
                серверными операционными системами.
            </div>
            <div class="phyton_txt">
                Чаще всего Python используют в веб-разработке. 
                Для него написано множество фреймворков: FastAPI, 
                Flask, Tornado, Pyramid, TurboGears, CherryPy и, самый популярный, Django.
            </div>
            <div class="phyton_txt">
                Ещё одна область применения Python — автоматизация тестирования. 
                Многие специалисты по автоматизации QA выбирают Python из-за его простоты. 
                Он отлично подходит тем, кто имеет небольшой опыт в разработке приложений. 
                Развитое сообщество, логичный синтаксис и удобочитаемость упрощают процесс обучения.
            </div>
            <div id="style_phyton">
                <img src="''' + url_for('static', filename='chris-ried-ieic5Tq8YMk-unsplash.jpg') + '''">
            </div>
        </body>
    </html>   
'''

@app.route('/lab1/something')
def something():
     return '''
   <!doctype html>
    <html>
        <head>
            <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1.css') + '''">
        </head>
        <body>
            <div class="something_txt">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam neque dui, 
                pulvinar non aliquet non, pellentesque vitae sapien. Sed vel metus a turpis 
                ultricies accumsan in vel ligula. Fusce ornare tristique magna. Ut in ornare ex. 
                Curabitur bibendum tempus dolor ac semper. Fusce malesuada turpis ac ipsum molestie, 
                ut imperdiet ex euismod. Nunc porta sit amet nisl sed lobortis. Proin laoreet tempus 
                erat, elementum tincidunt eros.
            </div>
            <div class="something_txt">
                Etiam iaculis tincidunt justo, ut tincidunt lorem. Vivamus et ex imperdiet, gravida massa 
                id, facilisis justo. In cursus dignissim neque, a consectetur eros ultrices sed. Nunc accumsan
                  consectetur euismod. Integer ut vehicula libero. Mauris fermentum congue varius. Nam sed nisi
                    nec arcu consequat fringilla.
            </div>
            <div class="something_txt">
                Ut vehicula pulvinar nulla, sed pharetra arcu auctor et. Vivamus vestibulum, ex sed imperdiet eleifend, 
                urna erat pellentesque lorem, at vehicula nibh massa sed sapien. Fusce ornare sed quam at condimentum. 
                Cras imperdiet nunc risus, nec accumsan nulla volutpat eget. Vestibulum varius, risus ac dignissim aliquam, 
                ipsum felis tempor nunc, eu gravida eros dolor finibus felis. Nunc convallis metus sit amet justo porttitor 
                venenatis. Cras sollicitudin justo enim. Sed tempor auctor justo ac scelerisque.
            </div>
            <div id="style_something">
                <img src="''' + url_for('static', filename='something.png') + '''">
            </div>
        </body>
    </html>   
'''