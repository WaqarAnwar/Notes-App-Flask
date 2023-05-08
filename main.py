from flask import Flask,request,render_template,redirect,url_for
from models import db,NoteModel 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

app.app_context().push()
db.create_all()
 

@app.route('/data/create' , methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('createpage.html')
 
    if request.method == 'POST':
        note = request.form['note']
        note = NoteModel(note=note)
        db.session.add(note)
        db.session.commit()
        return redirect('/data')
    
@app.route('/data')
def RetrieveDataList():
    notes = NoteModel.query.all()
    print(notes)
    return render_template('datalist.html',notes = notes)

@app.route('/data/<int:id>/delete', methods=['GET','POST'])
def deleteNote(id):
    note = NoteModel.query.filter_by(id=id).first()
    if note:
        db.session.delete(note)
        db.session.commit()
 
    return redirect(url_for('RetrieveDataList'))

def abc(id):
    return '<h1>id</h1>'


app.run(host='localhost', port=4000,debug=True)
