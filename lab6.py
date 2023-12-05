from flask import Blueprint,render_template, request, redirect, session
from werkzeug.security import check_password_hash, generate_password_hash
from db import db
from db.models import users, articles
from flask_login import login_user, login_required, current_user, logout_user

lab6 = Blueprint('lab6', __name__)

@lab6.route("/lab6/")
def lab():
    username = "Аноним" if current_user.is_anonymous else current_user.username
    return render_template('lab6.html', username=username)


@lab6.route("/lab6/check")
def main():
    my_users = users.query.all()
    print(my_users)
    return 'result in console'


@lab6.route("/lab6/checkarticles")
def checkarticles():
    my_articles = articles.query.all()
    print(my_articles)
    return 'result in console'


@lab6.route("/lab6/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template ("register2.html")
    
    username_form = request.form.get("username")
    password_form = request.form.get("password")

    if not username_form:
            errors = 'Имя не может быть пустым'

    elif len(password_form) < 5:
            errors = 'Пароль должен содержать не менее 5 символов'

    else:
            ifUserExist = users.query.filter_by(username=username_form).first()

            if ifUserExist:
                errors = 'Пользователь с таким именем уже существует'
            else:
                hashedPswd = generate_password_hash(password_form, method='pbkdf2')

                newUser = users(username=username_form, password=hashedPswd)

                db.session.add(newUser)
                db.session.commit()

                return redirect("/lab6/login")

    return render_template("register2.html", errors=errors)

@lab6.route("/lab6/login", methods=["GET", "POST"])
def login():
    errors = None

    if request.method == "POST":
        username_form = request.form.get("username")
        password_form = request.form.get("password")

        if not username_form or not password_form:
            errors = 'Имя пользователя и пароль должны быть заполнены'
        else:
            my_user = users.query.filter_by(username=username_form).first()

            if my_user is None:
                errors = 'Пользователь с таким именем не существует'
            else:
                if not check_password_hash(my_user.password, password_form):
                    errors = 'Неправильный пароль'
                else:
                    login_user(my_user, remember=False)
                    return redirect("/lab6/")

    return render_template("login3.html", errors=errors)
         

@lab6.route("/lab6/articles")
@login_required
def articles_list():
    my_articles = articles.query.filter_by(user_id=current_user.id).all()
    return render_template("list_articles.html", articles=my_articles)

@lab6.route("/lab6/articles/<int:article_id>")
@login_required
def article_details(article_id):
    article = articles.query.get(article_id)
    if article is not None and article.user_id == current_user.id:
        return f"Details of Article {article_id}: {article.title}; {article.article_text}"
    else:
        return "Access denied or article not found"
    

@lab6.route("/lab6/logout")
@login_required
def logout():
    logout_user()
    return redirect("/lab6")


@lab6.route("/lab6/articles")
@login_required
def articles_list_route():
    my_articles = articles.query.filter_by(user_id=current_user.id).all()
    return render_template("list_articles.html", articles=my_articles)


@lab6.route("/lab6/add_article", methods=["GET", "POST"])
@login_required
def add_article():
    errors = None

    if request.method == "POST":
        title = request.form.get("title")
        article_text = request.form.get("article_text")

        if not title or not article_text:
            errors = 'Заголовок и текст статьи должны быть заполнены'
        else:
            new_article = articles(title=title, article_text=article_text, user_id=current_user.id)

            db.session.add(new_article)
            db.session.commit()

            return redirect("/lab6/articles")

    return render_template("add_article.html", errors=errors)