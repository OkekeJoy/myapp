from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_sqlalchemy import SQLAlchemy

tapp= Flask(__name__)
tapp.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://postgres:break@localhost:5432/example'
tapp.config['SQLALCHEMY_TRACK_MODIFICATIONS']= True
db= SQLAlchemy(tapp)

class todo(db.Model):
    id= db.Column(db.Integer(), primary_key= True)
    description= db.Column(db.String(), nullable=False)
db.create_all()


todo1= todo(description= "Ist thing to do")
todo2= todo(description= "2nd thing to do")
todo3= todo(description= "3rd thing to do")
db.session.add_all([todo1, todo2, todo3])
db.session.commit()

def _repr_(self):
    return f'<todo {self.id} {self.description}>'


@tapp.route('/todo/create', methods=['POST'])
def create_todo():
    description= request.get_json()['description']
    todo4= todo(description=description)
    db.session.add(todo4)
    db.session.commit()
    return jsonify({'description':todo4.description})
    
@tapp.route('/')
def index():
    return render_template('dex.html', data=todo.query.all())




if __name__ == '__main__':
    tapp.debug= True
    tapp.run(host='0.0.0.0')