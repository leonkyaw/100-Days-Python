from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
from dotenv import load_dotenv
import os

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
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
load_dotenv()
API_KEY = os.getenv('API_KEY')
HEADERS = {
    "accept": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}


# CREATE DB
class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///favorite_movies.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE TABLE
class Movies(db.Model):
    id: Mapped[int] = mapped_column(Integer, unique=True, primary_key=True)
    title: Mapped[str] = mapped_column(String(500), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[str] = mapped_column(Float, nullable=True)
    ranking: Mapped[str] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


# adding records
# second_movie = Movies(
#     title="Avatar The Way of Water",
#     year=2022,
#     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#     rating=7.3,
#     ranking=9,
#     review="I liked the water.",
#     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
# )
# with app.app_context():
#     # db.session.add(second_movie)
#     # db.session.commit()


# Create form for Edit
class EditForm(FlaskForm):
    rating = StringField(label="Your Rating out of 10 eg: 8.7", validators=[DataRequired()])
    review = StringField(label="Your Review", validators=[DataRequired()])
    submit = SubmitField(label="Done")


# Create form for Add
class AddForm(FlaskForm):
    title = StringField(label="Movie Title", validators=[DataRequired()])
    submit = SubmitField(label="Add Movie")


@app.route("/")
def home():
    result = db.session.execute(db.select(Movies).order_by(Movies.rating))  # Ascending order is the default
    all_movies = result.scalars().all()  # convert ScalarResult to Python list

    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()

    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=['POST', 'GET'])
def edit():
    form = EditForm()
    selected_id = request.args.get('id')
    selected_movie = db.get_or_404(Movies, selected_id)
    if form.validate_on_submit():
        selected_movie.rating = request.form['rating']  # form.rating.data
        selected_movie.review = request.form['review']  # form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", form=form, movie=selected_movie.title)


@app.route('/delete')  # no need POST/GET as we are not working with form here
def delete():
    selected_id = request.args.get('id')
    selected_movie = db.get_or_404(Movies, selected_id)
    db.session.delete(selected_movie)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/add', methods=['POST', 'GET'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        params = {
            "query": f"{form.title.data}"
        }
        response = requests.get("https://api.themoviedb.org/3/search/movie?include_adult=false&language=en-US&page=1",
                                params=params, headers=HEADERS)
        data = response.json()['results']
        return render_template('select.html', movies=data)
    return render_template('add.html', form=form)


@app.route('/find')
def find_movie():
    movie_id = request.args.get('id')

    if movie_id:
        movie_url = f"https://api.themoviedb.org/3/movie/{movie_id}"
        response = requests.get(movie_url, params={"language": "en-US"}, headers=HEADERS)
        data = response.json()
        new_movie = Movies(title=data['title'],
                           year=data['release_date'].split("-")[0],
                           img_url=f"https://image.tmdb.org/t/p/w500{data['poster_path']}",
                           description=data['overview'])
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('edit', id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
