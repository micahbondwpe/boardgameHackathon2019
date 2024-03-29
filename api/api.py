from datetime import datetime
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_bcrypt import Bcrypt
import json
import os

#Init App
app = Flask(__name__)
CORS(app)
basedir = os.path.abspath(os.path.dirname(__file__))
bcrypt = Bcrypt(app)

#Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Init DB
db = SQLAlchemy(app)

#Init ma
ma =Marshmallow(app)

# Boardgame Class/Model

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

@app.route('/boardgame/<id>', methods=['GET'])
def get_boardgame(id):
    boardgame = Boardgame.query.get(id)
    return boardgame_schema.jsonify(boardgame)


if __name__ == '__main__':
    app.run(debug=True)