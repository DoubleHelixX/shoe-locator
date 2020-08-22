import os
from sqlalchemy import (
  Column,
  String,
  Integer,
  create_engine,
  select,
  func,
  DateTime
)
from constants import (
  database_setup,
  jsonData
)
from sqlalchemy.orm import column_property
from flask_sqlalchemy import SQLAlchemy
import json
from flask import Flask
import pandas as pd
# from manage import migration
# ------------------------------------------------------------------------------------------------------#
# *                        Configures DB connection
# *                                  and
# *               Binds flask application to SQLAlchemy service
# ------------------------------------------------------------------------------------------------------#
# *Global use or Local use (defaults to local if global isn't found)
database_path = os.environ.get('DATABASE_URL', "postgres://{}:{}@{}/{}".format(
    database_setup["user_name"], database_setup["password"], database_setup["port"], database_setup["database_name"]))

# ! OR just Local use below:
#  # database_path ="postgresql+psycopg2://{}:{}@{}/{}".format(database_setup['user_name'], database_setup['password'], database_setup['port'], database_setup['database_name'])

# ! For intergrating PANDAS
#  engine = create_engine(database_path)

db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()
    # migration(app,db)


# ------------------------------------------------------------------------------------------------------#
# *              Functions for dropping, creating, and initializing data within the database
# ------------------------------------------------------------------------------------------------------#
# *Drops and creates tables
def db_drop_and_create_all():
    db.drop_all()
    db.create_all()


# * Using CSV with Pandas
def db_initialize_tables_csv_pandas():
    engine = db.get_engine()
    csv_file_path = 'C:/Users/Public/bays_.csv'
    #  Read CSV with Pandas
    df = pd.read_csv(csv_file_path)
    print(df)
    #  Insert to DB
    df.to_sql('bays',
              con=engine,
              index=True,
              index_label='id',
              if_exists='replace')

# * Using Stored constant dictionary variables as the JSON data


def db_initialize_tables_json():
    for i in jsonData:
        # print(i)
        for j in i['data']:
            new_bay = (Bay(
                bay=i['bay'],
                section=j['section'],
                name=j['name'],
                style=j['style'],
                row=j['row'],
                col=j['col'],
                notes=j['notes'],
                gender=j['gender'],
                img=j['img'],
            ))
            new_bay.insert()


# *----------------------------------------------------------------------------#
# *                            Models - ORM
# *----------------------------------------------------------------------------#


class Bay(db.Model):
    __tablename__ = 'bays'

    id = db.Column(db.Integer, primary_key=True)
    bay = db.Column(db.Integer, nullable=False)
    section = db.Column(db.String(120), nullable=False)
    name = db.Column(db.String(120))
    style = db.Column(db.String(120), nullable=False)
    row = db.Column(db.String(120), nullable=False)
    col = db.Column(db.String(120), nullable=False)
    notes = db.Column(db.String(120))
    img = db.Column(db.String(500), nullable=True)
    gender = db.Column(db.CHAR(1))
    data = db.relationship('Data', backref='bays', lazy=True)

    def __repr__(self):
        return f'<Bay {self.id} {self.name}>'

    def __init__(self,
                 bay, section, name,
                 style, row, col,
                 notes, img, gender):
        self.bay = bay
        self.section = section
        self.name = name
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


class Data(db.Model):
    __tablename__ = 'data'

    id = db.Column(db.Integer, primary_key=True)
    bayId = db.Column(db.Integer, db.ForeignKey('bays.id'), nullable=True)
    shoeCount = db.Column(db.Integer, nullable=True)
    date_added = Column(DateTime())

    def __repr__(self):
        return f'<Bay {self.id} {self.date_added}>'

    def __init__(self, bayId, shoeCount, date_added):
        self.bayId = bayId
        self.shoeCount = shoeCount
        self.date_added = date_added

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
            'bayId': self.bayId,
            'shoeCount': self.shoeCount,
            'date_added': self.date_added
        }

# ----------------------------------------------------------------------------#
#  Filters.
# ----------------------------------------------------------------------------#


#  def format_datetime(value, format='medium'):
#    date = dateutil.parser.parse(value)
#    if format == 'full':
#        format = "EEEE MMMM, d, y 'at' h:mma"
#    elif format == 'medium':
#        format = "EE MM, dd, y h:mma"
#    return babel.dates.format_datetime(date, format)


#  app.jinja_env.filters['datetime'] = format_datetime
