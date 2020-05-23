from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from model.abstract_dairy_product import AbstractDairyProduct
import os
import json
import copy

with open('secret.json') as f:
    SECRET = json.load(f)

DB_URI = "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}".format(
    user=SECRET["user"],
    password=SECRET["password"],
    host=SECRET["host"],
    port=SECRET["port"],
    db=SECRET["db"])

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class DairyProduct(AbstractDairyProduct, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    warranty_period_in_days = db.Column(db.Integer)
    price_in_uah = db.Column(db.Float)
    producer = db.Column(db.String(32))
    producing_country = db.Column(db.String(32))
    fat_content_in_percentage = db.Column(db.Float)

    def __init__(self, warranty_period_in_days, price_in_uah, producer,
                 producing_country, fat_content_in_percentage):
        super().__init__(warranty_period_in_days, price_in_uah, producer, producing_country,
                         fat_content_in_percentage)


class DairyProductSchema(ma.Schema):
    class Meta:
        fields = ('warranty_period_in_days', 'price_in_uah',
                  'producer', 'producing_country', 'fat_content_in_percentage')


dairy_product_schema = DairyProductSchema()
dairy_products_schema = DairyProductSchema(many=True)


@app.route("/dairy_product", methods=["POST"])
def add_dairy_product():
    warranty_period_in_days = request.json['warranty_period_in_days']
    price_in_uah = request.json['price_in_uah']
    producer = request.json['producer']
    producing_country = request.json['producing_country']
    fat_content_in_percentage = request.json['fat_content_in_percentage']

    cheese = DairyProduct(warranty_period_in_days, price_in_uah,
                          producer, producing_country, fat_content_in_percentage)

    db.session.add(cheese)
    db.session.commit()
    return dairy_product_schema.jsonify(cheese)


@app.route("/dairy_product", methods=["GET"])
def get_all_dairy_products():
    all_db_cheeses_schema = DairyProduct.query.all()
    response = dairy_products_schema.dump(all_db_cheeses_schema)
    return jsonify({'dairy_product_schema': response})


@app.route("/dairy_product/<id>", methods=["GET"])
def dairy_product_info(id):
    dairy_product = DairyProduct.query.get(id)
    if not dairy_product:
        abort(404)
    return dairy_product_schema.jsonify(dairy_product)


@app.route("/dairy_product/<id>", methods=["PUT"])
def update_dairy_product(id):
    dairy_product = DairyProduct.query.get(id)
    if not dairy_product:
        abort(404)
    old_dairy_product = copy.deepcopy(dairy_product)
    dairy_product._warranty_period_in_days = request.json['warranty_period_in_days']
    dairy_product.price_in_uah = request.json['price_in_uah']
    dairy_product.producer = request.json['producer']
    dairy_product.producing_country = request.json['producing_country']
    dairy_product.fat_content_in_percentage = request.json['fat_content_in_percentage']
    db.session.commit()
    return dairy_product_schema.jsonify(old_dairy_product)


@app.route("/dairy_product/<id>", methods=["DELETE"])
def delete_dairy_product(id):
    dairy_product = DairyProduct.query.get(id)
    if not dairy_product:
        abort(404)
    db.session.delete(dairy_product)
    db.session.commit()
    return dairy_product_schema.jsonify(dairy_product)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='127.0.0.1')
