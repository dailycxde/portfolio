from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    img = db.Column(db.String)
    desc = db.Column(db.String)

    def __repr__(self):
        return f'Project Name: {self.name}'

class Community(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    img = db.Column(db.String)
    role = db.Column(db.String(20))
    url = db.Column(db.String);

    def __repr__(self):
        return f'Community Name: {self.name}'

@app.route('/')
def home():
    projects = Project.query.all()
    communities = Community.query.all()
    return render_template('index.html', projects=projects, communities=communities)


if __name__ == '__main__':
    app.run(debug=True)