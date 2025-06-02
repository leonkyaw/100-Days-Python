from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random
'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        # Method 1.
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            # Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary

        # Method 2. Altenatively use Dictionary Comprehension to do the same thing.
        # return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")  # doesn't need to use method=['GET'] as by default, it is GET method
def get():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()  # this is python list
    random_cafe = random.choice(all_cafes)
    return jsonify(cafe=random_cafe.to_dict())


@app.route('/all')
def get_all():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()  # Python List
    return jsonify(cafe=[cafe.to_dict() for cafe in all_cafes])


@app.route('/search')
def search_cafe():
    location = request.args.get("loc")
    result = db.session.execute(db.select(Cafe).where(Cafe.location == location))
    cafe_list = result.scalars().all()
    if cafe_list:
        return jsonify(cafe=[cafe.to_dict() for cafe in cafe_list])
    else:
        return jsonify(error={"Not Found": "Sorry we don't have a cafe at that location"}), 404


# HTTP POST - Create Record
@app.route('/add', methods=['POST', 'GET'])
def add_cafe():
    new_cafe = Cafe(name=request.form.get("name"),
                    map_url=request.form.get("map_url"),
                    seats=request.form.get("seats"),
                    location=request.form.get("location"),
                    img_url=request.form.get("img_url"),
                    has_wifi=bool(request.form.get("has_wifi")),
                    has_toilet=bool(request.form.get("has_toilet")),
                    has_sockets=bool(request.form.get("has_sockets")),
                    coffee_price=request.form.get("coffee_price"),
                    can_take_calls=bool(request.form.get("can_take_calls")))
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


# HTTP PUT/PATCH - Update Record
@app.route('/update/<int:cafe_id>', methods=['PATCH'])
def update(cafe_id):
    try:
        result = db.get(Cafe, cafe_id)
    except AttributeError:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        result.coffee_price = request.args.get('new_price')
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}), 200


# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    if api_key == "TopSecretAPIKey":
        try:
            cafe = db.get(Cafe, cafe_id)
        except AttributeError:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
        else:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403


if __name__ == '__main__':
    app.run(debug=True)

