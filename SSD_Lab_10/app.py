from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'secretkey'


db = SQLAlchemy(app)

class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement = False)
    name = db.Column(db.String(80),nullable=False)
    stream = db.Column(db.String(80),nullable=False)

@app.route("/create", methods = ['POST'])
def create():
    if(request.method=='POST'):
        data = request.get_json()
        id = data['id']
        name = data['name']
        stream = data['stream']
        check_user = Students.query.filter_by(id=id).first()
        if(check_user is not None):
            return "id already exists"
        else:
            data = Students(id = id, name=name,stream = stream)
            db.session.add(data)
            db.session.commit()
            return "added successfully"

@app.route("/read",methods = ['GET'])
def read():
    if(request.method=='GET'):
        data = Students.query.all()
        if( data is not None):
            d={}
            for user in data:
                d[user.id] = {'name':user.name , 'stream':user.stream}
            return jsonify(d)
        else:
            return "no data found"

@app.route("/update",methods = ['PUT'])
def update():
     if(request.method=='PUT'):
        data = request.get_json()
        id = data['id']
        name = data['name']
        stream = data['stream']
        check_user = Students.query.filter_by(id=id).first()
        if(check_user is None):
            return "id not found"
        else:
            Students.query.filter(id == id).update({'name' : name,'stream': stream})
            db.session.commit()
            return "Update success"


@app.route("/delete/<int:id>",methods = ['DELETE'])
def delete(id):
    if(request.method=='DELETE'):
        check_user = Students.query.filter_by(id=id).first()
        if(check_user is None):
            return "id not found"
        else:
            Students.query.filter_by(id=id).delete()
            db.session.commit()
            return "Delete success"

if(__name__ == '__main__'):
    app.run(port=8000,debug=True)






