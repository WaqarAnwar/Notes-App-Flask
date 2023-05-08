from flask_sqlalchemy import SQLAlchemy
import uuid
 
db = SQLAlchemy()
 
class NoteModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    note = db.Column(db.String())
 