from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"

# Create the extension
db = SQLAlchemy(model_class=Base)
# Initialise the app with extension
db.init_app(app)


#Create Table
class Books(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    title: Mapped[str] = mapped_column(unique=True, nullable=False)
    author: Mapped[str] = mapped_column(nullable=False)
    rating: Mapped[float] = mapped_column(nullable=False)


# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    result = db.session.execute(db.select(Books).order_by(Books.title))
    all_books = result.scalars().all()
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        new_book = Books(title=request.form['title'],
                         author=request.form['author'],
                         rating=request.form['rating'])
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('add.html')


@app.route('/edit_rating', methods=["POST","GET"])
def edit():
    if request.method == 'POST':
        book_id = request.form['id']
        book_to_update = db.get_or_404(Books,book_id)
        book_to_update.rating = request.form['rating']
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = db.get_or_404(Books, book_id)
    return render_template('edit_rating.html', book=book_selected)


@app.route('/delete')
def delete():
    book_id = request.args.get('id')

    # Delete the record
    book_to_delete = db.get_or_404(Books, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

