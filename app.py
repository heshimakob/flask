from email.policy import default
from msilib.schema import Class
import sqlite3
from typing_extensions import Self
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from sqlalchemy import null

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///todo.db'
db=SQLAlchemy(app)
class Task(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.column(db.String(80), nullable=False)
    created_at=db.column(db.DateTime,nullable=False, default=datetime.utcnow)

    def __repre__(Self):
        return f"todo{self.name}"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about/")
def about():
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True)
