from werkzeug.security import check_password_hash, generate_password_hash
from flask import Blueprint,render_template, request, redirect, session
import psycopg2


lab5 = Blueprint('lab5', __name__)


def dbConnect():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="knowledge_base",
        user="denis_knowledge_base_",
        password="321")

    return conn;


def dbClose(cursor, connection):
    cursor.close()
    connection.close()


@lab5.route('/lab5/')
def main():
    visibleUser = session.get('username', 'Anon')

    return render_template('lab5.html', username = visibleUser)


@lab5.route('/lab5/register', methods = ["GET", "POST"])
def registerPage():
    errors = []

    if request.method == "GET":
        return render_template('register.html', errors = errors)
    
    username = request.form.get("username")
    password = request.form.get("password")

    if not (username and password):
        errors.append('Пожалуйста заполните все поля')
        print(errors)
        return render_template('register.html', errors = errors)
    
    hashPassword = generate_password_hash(password)
    
    conn = dbConnect()
    cur = conn.cursor()

    cur.execute("SELECT username FROM users WHERE username = %s;", (username))

    if cur.fetchone() is not None:
        errors.append("Пользователь с данным именем уже существует")

        dbClose(cur, conn)

        return render_template('register.html', errors=errors)
    
    cur.execute("INSERT INTO users (username, password) VALUES (%s, %s);", (username, hashPassword))

    conn.commit()
    dbClose(cur, conn)

    return redirect("/lab5/login")


@lab5.route('/lab5/login', methods = ["GET", "POST"])
def loginPage():
    errors = []

    if request.method == "GET":
        return render_template('login2.html', errors = errors)
    
    username = request.form.get("username")
    password = request.form.get("password")

    if not (username and password):
        errors.append('Пожалуйста заполните все поля')
        return render_template('login2.html', errors = errors)
    
    
    conn = dbConnect()
    cur = conn.cursor()

    cur.execute("SELECT id, password FROM users WHERE username = %s;", (username,))

    result = cur.fetchone()

    if result is None:
        errors.append("Неправильный логин или пароль")

        dbClose(cur, conn)

        return render_template('login2.html', errors=errors)
    
    userID, hashPassword = result

    if check_password_hash(hashPassword, password):
        session['id'] = userID
        session['username'] = username
        dbClose(cur, conn)
        return redirect("/lab5/")
    
    else:
        errors.append("Неправильный пароль или логин")
        return render_template("login2.html", errors=errors, username=username)
    

@lab5.route('/lab5/new_article', methods = ["GET", "POST"])
def createArticle():
    errors = []

    userID = session.get("id")
    username = session.get("username")

    if userID is not None:
        if request.method == "GET":
            return render_template("new_article.html", username = username)
        
        if request.method == "POST":
            text_article = request.form.get("text_article")
            title = request.form.get("title_article")

            if len(text_article) == 0:
                errors.append("Заполните текст")
                return render_template("new_article.html", errors=errors, username = username)
            
            conn = dbConnect()
            cur = conn.cursor()

            cur.execute("INSERT INTO articles(user_id, title, article_text) VALUES (%s, %s,%s) RETURNING id", (userID, title, text_article))

            new_article_id = cur.fetchone()[0]
            conn.commit()

            dbClose(cur, conn)

            return redirect (f"/lab5/articles/{new_article_id}")
    
    return redirect('/lab5/login')


@lab5.route('/lab5/articles/<int:article_id>', methods = ["GET", "POST"])
def getArticle(article_id):

    userID = session.get("id")

    if userID is not None:
        conn = dbConnect()
        cur = conn.cursor()

        cur.execute("SELECT title, article_text FROM articles WHERE id = %s and user_id = %s", (article_id, userID))

        articleBody = cur.fetchone()

        dbClose(cur, conn)

        if articleBody is None:
            return "Not found!"
        
        text = articleBody[1].splitlines()

        return render_template("articleN.html", article_text = text, article_title = articleBody[0], username = session.get("username"))
        

@lab5.route('/lab5/user_articles')
def userArticles():
    user_id = session.get('id')
    username = session.get('username')

    if user_id is not None:
        conn = dbConnect()
        cur = conn.cursor()

        cur.execute("SELECT id, title, article_text FROM articles WHERE user_id = %s", (user_id,))
        articles = cur.fetchall()

        dbClose(cur, conn)

        return render_template('user_articles.html', user_articles=articles, username=username)
    else:
        return redirect('/lab5/login')
    

@lab5.route('/lab5/logout')
def logout():
    session.clear()  # Очистка данных пользовательской сессии, включая JWT-токен
    return redirect('/lab5/')  # Перенаправление пользователя на главную страницу или иную страницу как вам угодно


@lab5.route('/lab5/users')
def users():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="knowledge_base",
        user="denis_knowledge_base_",
        password="321"
    )
    cur = conn.cursor()

    cur.execute("SELECT * FROM users;")

    result = cur.fetchall()

    cur.close()
    conn.close()
    return render_template('users.html', result=result)


#@lab5.route('/lab5/publish_article/<int:article_id>', methods=["GET"])
#def publishArticle(article_id):
#    conn = dbConnect()
#    cur = conn.cursor()
#    cur.execute("UPDATE articles SET is_public = True WHERE id = %s", (article_id,))
#    conn.commit()
#    dbClose(cur, conn)
#    return redirect("/lab5/articleN/%s", (article_id))
#
#
#@lab5.route('/lab5/add_to_favorites/<int:article_id>', methods=["GET"])
#def addToFavorites(article_id):
#    user_id = session.get("id")
#    if user_id:
#        conn = dbConnect()
#        cur = conn.cursor()
#        cur.execute("UPDATE articles SET is_favorite = True WHERE id = %s", (article_id,))
#        conn.commit()
#        dbClose(cur, conn)
#    return redirect("/lab5/articles/%s", (article_id))
#
#
#@lab5.route('/lab5/publish_article/<int:article_id>', methods=["GET"])
#def publishArticle(article_id):
#    conn = dbConnect()
#    cur = conn.cursor()
#    cur.execute("UPDATE articles SET is_public = True WHERE id = %s", (article_id,))
#    conn.commit()
#    dbClose(cur, conn)
#    return redirect("/lab5/articles/%s", (article_id))