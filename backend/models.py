import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
import manage as m

database_name = "shoe_locate"
database_path = "postgresql+psycopg2://{}:{}@{}/{}".format('postgres', '1','localhost:5432', database_name)

db = SQLAlchemy()
migration=None
'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
  try:
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    # db.drop_all()
    # db.create_all()
    # BOOTSTRAP DB migration command with migration file
    migration = m.migration(app, db)
    return True
  except:
    return False



#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#


class Bay(db.Model):
  __tablename__ = 'bays'

  id = db.Column(db.Integer, primary_key=True)
  bay = db.Column(db.Integer, nullable=False)
  section = db.Column(db.String(120), nullable=False)
  name = db.Column(db.String)
  style = db.Column(db.String(120), nullable=False)
  row = db.Column(db.String(120), nullable=False)
  col = db.Column(db.String(120), nullable=False)
  notes = db.Column(db.String(120))
  img = db.Column(db.String(500), nullable = True)
  gender = db.Column(db.CHAR(1))
  
  def __repr__(self):
    return f'<Bay {self.id} {self.name}>'
  
  def __init__(self, bay, section, name, style, row, col, notes, img, gender):
    self.bay = bay
    self.section = section
    self.name =name
    self.style = style
    self.row = row
    self.col = col
    self.notes = notes
    self.img = img
    self.gender = gender
    

  def insert(self):
    db.session.add(self)
    db.session.commit()
    
  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'bay': self.bay,
      'section': self.section,
      'name': self.name,
      'style': self.style,
      'row': self.row,
      'col': self.col,
      'notes': self.notes,
      'img': self.img,
      'gender': self.gender.upper()
    }

#----------------------------------------------------------------------------#
# Filters.
#----------------------------------------------------------------------------#


# def format_datetime(value, format='medium'):
#   date = dateutil.parser.parse(value)
#   if format == 'full':
#       format = "EEEE MMMM, d, y 'at' h:mma"
#   elif format == 'medium':
#       format = "EE MM, dd, y h:mma"
#   return babel.dates.format_datetime(date, format)


# app.jinja_env.filters['datetime'] = format_datetime

