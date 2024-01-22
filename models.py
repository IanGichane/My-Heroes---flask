from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# If you want to use many-to-many relationships you will need to define a helper table that is used for the relationship. It will basically holds the primary keys of both tables.
hero_power = db.Table('hero_power',
                     db.Column('hero_id', db.Integer, db.ForeignKey('hero.id')),
                     db.Column('power_id', db.Integer, db.ForeignKey('power.id')),
                    
                     )

class Hero(db.Model):
    __tablename__='hero'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=False)
    super_name = db.Column(db.String, nullable=False)

   
    powers = db.relationship('Power', secondary='hero_power', back_populates='heroes')

    def __repr__(self):
        return f'<Hero(id={self.id}, super_name={self.super_name}, description={self.description})>'

class Power(db.Model):
    __tablename__='power'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=False)
    description =db.Column(db.Text)
    heroes = db.relationship('Hero', secondary='hero_power', back_populates='powers')

    def __repr__(self):
        return f'<Power(id={self.id}, name={self.name}, description={self.description})>'




