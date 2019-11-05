from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import json
import os
import argparse

# initiate the parser
parser = argparse.ArgumentParser()
parser.add_argument("filename", help="set filename")
args = parser.parse_args()

#Init App
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

#Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Init DB
db = SQLAlchemy(app)

#Init ma
ma =Marshmallow(app)

class Boardgame(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    minplayers = db.Column(db.Integer, nullable=False)
    maxplayers = db.Column(db.Integer, nullable=False)
    playingtime = db.Column(db.Integer, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    boardgamecategory = db.Column(db.String(512), nullable=False)
    boardgamemechanic = db.Column(db.String(512), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(512))
    thumbnail = db.Column(db.String(512))
    
    def __init__(self, id, name, minplayers, maxplayers, playingtime, age, boardgamecategory, boardgamemechanic, rating, image, thumbnail):
        self.id = id
        self.name = name
        self.minplayers = minplayers
        self.maxplayers = maxplayers
        self.playingtime = playingtime
        self.age = age
        self.boardgamecategory = boardgamecategory
        self.boardgamemechanic = boardgamemechanic
        self.rating = rating
        self.image = image
        self.thumbnail = thumbnail

class BoardgameSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'minplayers', 'maxplayers', 'playingtime', 'age', 'boardgamecategory', 'boardgamemechanic', 'rating', 'image', 'thumbnail')

boardgame_schema = BoardgameSchema(strict=True)
boardgames_schema = BoardgameSchema(many=True, strict=True)

with open(f"../json/{args.filename}", "r") as read_file:
    data = json.load(read_file)
    id = data["id"]
    name = data["name"]
    minplayers = data["minplayers"]
    maxplayers = data["maxplayers"]
    playingtime = data["playingtime"]
    age = data["age"]
    boardgamecategory = data["boardgamecategory"]
    boardgamemechanic = data["boardgamemechanic"]
    rating = data["rating"]
    image = data["image"]
    thumbnail = data["thumbnail"]

    new_row = Boardgame(id, name, minplayers, maxplayers, playingtime, age, boardgamecategory, boardgamemechanic, rating, image, thumbnail)
    db.session.add(new_row)
    db.session.commit()