from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

tapp= Flask(__name__)
tapp.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://postgres:break@localhost:5432/example'

db= SQLAlchemy(tapp)

class TODO(db.Model):
    id= db.Column(db.Integer(), primary_key= True)
    description= db.Column(db.String(), nullable=False)
    db.create_all()


if __name__ == '__main__':
    tapp.debug= True
    tapp.run ('0.0.0.0')