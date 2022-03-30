from flask import Flask, render_template, url_for, request
from books_recommend import get_recommendations
import psycopg2
import psycopg2.extras

app = Flask(__name__)

Host = <--Host Name-->
Database = <--DB Name-->
User = <--User Name-->
Port = 5432
Password = <--Pasword-->

def get_db_connection():
    conn = psycopg2.connect(host=Host,
                            database=Database,
                            user=User,
                            password=Password)
    return conn


@app.route('/', methods = ['POST','GET'])
def index():
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    cursor.execute("SELECT * from <--TABLE NAME-->")
    data = cursor.fetchall()
    
    if request.method == "POST":
        book_name = request.form.get("book_name")
        books = get_recommendations(book_name)

        return render_template('index.html',
                                books = books,
                                book_name = book_name,
                                data = data)
    else:
        return render_template('index.html',data = data)

if __name__ == "__main__":
    app.run(debug=True)